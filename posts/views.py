from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from .models import Post
from django.db.models import Q, Count, Case, When
from comentarios.forms import FormComentario
from comentarios.models import Comentario
from django.contrib import messages 
from django.views import View

#Utilizando classes onde a vantagem  é que você pode reutilizar o codigo com o sistema de heranças


class PostIndex(ListView):
    model = Post
    template_name = 'posts/index.html'
    paginate_by = 6
    context_object_name = 'posts'

    #ordenar os post de forma invertida e filtrando itens publicados apenas
    def get_queryset(self):
        qs =  super().get_queryset()
        qs = qs.select_related('categoria_post')
        qs = qs.order_by('-id').filter(publicado_post=True)

    #obeter numero de comentarios caso ele esteja postado = True
        qs = qs.annotate(
            #Caso/quando o comentario estiver publicado conte 1
            numero_comentarios=Count(
                Case(
                    When(comentario__publicado_comentario=True, then=1)
                )
            )

        )
        return qs
    

class PostBusca(PostIndex):
    template_name = 'posts/post_busca.html'

    def get_queryset(self):
        qs = super().get_queryset()
        termo = self.request.GET.get('termo')

        #caso a busca não seja encontrada ele retorna o proprio qs
        if not termo:
            return qs

        qs = qs.filter(
            Q(titulo_post__icontains=termo) |
            Q(autor_post__first_name__iexact=termo) |
            Q(conteudo_post__icontains=termo) |
            Q(excerto_post__icontains=termo) |
            Q(categoria_post__nome_cat__iexact=termo)
        )

        return qs
    

class PostCategoria(PostIndex):
    template_name = 'posts/post_categoria.html'

    def get_queryset(self):
        qs =  super().get_queryset()

        categoria = self.kwargs.get('categoria', None)

        if not categoria:
            return   qs

        qs = qs.filter(categoria_post__nome_cat__iexact=categoria)

        return qs
    

# class PostDetalhes(UpdateView):
#     template_name = 'posts/post_detalhes.html'
#     model = Post
#     form_class =  FormComentario
#     context_object_name = 'post'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         post = self.get_object()
#         comentarios = Comentario.objects.filter(
#             publicado_comentario=True,
#             post_comentario = post.id)
#         context['comentarios'] = comentarios


#         return context
    


#     def form_valid(self, form):
#         post = self.get_object()
#         comentario = Comentario(**form.cleaned_data)
#         comentario.post_comentario = post

#         if self.request.user.is_authenticated:
#             comentario.usuario_comentario =  self.request.user
            
        
#         comentario.save()
#         messages.success(self.request, 'Comentario postado com sucesso!') 
#         return redirect('post_detalhes', pk=post.id)

class PostDetalhes(View):
    template_name = 'posts/post_detalhes.html'

    def setup(self, request,*args, **kwargs):
        super().setup(request, *args, **kwargs)

        pk = self.kwargs.get('pk')
        post = get_object_or_404(Post, pk=pk, publicado_post=True)

        self.contexto = {
            'post': post,
            'comentarios': Comentario.objects.filter(post_comentario=post, 
            publicado_comentario=True),
            'form': FormComentario(request.POST or None),
        }


    def get(self, request, *args, **kwargs):
        return render (request, self.template_name, self.contexto)

    def post(self, request, *args, **kwargs):
        form = self.contexto['form']
        
        if not form.is_valid():
            return render (request, self.template_name, self.contexto)

        comentario = form.save(commit=False)

        if request.user.is_authenticated:
            comentario.usuario_comentario = request.user

        comentario.post_comentario = self.contexto['post']
        comentario.save()
        messages.success(request, 'Seu comentário foi enviado para revisão!')
        return redirect('post_detalhes', pk=self.kwargs.get('pk'))








# Create your views here.

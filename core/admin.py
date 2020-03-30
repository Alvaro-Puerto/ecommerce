from django.contrib import admin
from .models import (Slider,
                    Articulo,
                    ImagenRefencia,
                    Categorias,
                    Pedido,
                    ArticuloPedido
                    )

admin.site.register(Slider)
admin.site.register(Articulo)
admin.site.register(ImagenRefencia)
admin.site.register(Categorias)
admin.site.register(Pedido)
admin.site.register(ArticuloPedido)
from django.contrib import admin


from .models import AtaChapters,FsgCodes,GtipCodes,ProductDocumentSources,ProductDocumentTypes,ProductDocuments,ProductImages,ProductInformation,Products,NatoStocks

admin.site.register(AtaChapters)
admin.site.register(FsgCodes)
admin.site.register(GtipCodes)
admin.site.register(Products)
admin.site.register(ProductDocumentTypes)
admin.site.register(ProductDocumentSources)
admin.site.register(ProductDocuments)
admin.site.register(ProductImages)
admin.site.register(ProductInformation)
admin.site.register(NatoStocks)



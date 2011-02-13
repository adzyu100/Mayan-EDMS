from django.contrib import admin

from models import MetadataType, DocumentType, Document, \
    DocumentTypeMetadataType, DocumentMetadata, DocumentTypeFilename, \
    MetadataIndex, DocumentMetadataIndex, DocumentPage, MetadataGroup, \
    MetadataGroupItem, DocumentTransformation


class MetadataTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'default', 'lookup')


class MetadataIndexInline(admin.StackedInline):
    model = MetadataIndex
    extra = 1
    classes = ('collapse-open',)
    allow_add = True

    
class DocumentTypeMetadataTypeInline(admin.StackedInline):
    model = DocumentTypeMetadataType
    extra = 1
    classes = ('collapse-open',)
    allow_add = True


class DocumentTypeFilenameInline(admin.StackedInline):
    model = DocumentTypeFilename
    extra = 1
    classes = ('collapse-open',)
    allow_add = True


class DocumentTypeAdmin(admin.ModelAdmin):
    inlines = [DocumentTypeFilenameInline, DocumentTypeMetadataTypeInline, MetadataIndexInline]


class DocumentMetadataInline(admin.StackedInline):
    model = DocumentMetadata
    extra = 0
    classes = ('collapse-open',)
    allow_add = False
    readonly_fields = ('metadata_type', 'value')  


class DocumentMetadataIndexInline(admin.StackedInline):
    model = DocumentMetadataIndex
    extra = 1
    classes = ('collapse-open',)
    allow_add = True
    readonly_fields = ('metadata_index', 'filename')


class DocumentPageInline(admin.StackedInline):
    model = DocumentPage
    extra = 1
    classes = ('collapse-open',)
    allow_add = True


class DocumentTransformationline(admin.StackedInline):
    model = DocumentTransformation
    extra = 1
    classes = ('collapse-open',)
    allow_add = True
    

class DocumentAdmin(admin.ModelAdmin):
    inlines = [DocumentMetadataInline, DocumentMetadataIndexInline, 
        DocumentTransformationline, DocumentPageInline]
    list_display = ('uuid', 'file_filename', 'file_extension')


class MetadataGroupItemInline(admin.StackedInline):
    model = MetadataGroupItem
    extra = 1
    classes = ('collapse-open',)
    allow_add = True
    
    
class MetadataGroupAdmin(admin.ModelAdmin):
    inlines = [MetadataGroupItemInline]
    filter_horizontal = ['document_type']
    
   
admin.site.register(MetadataType, MetadataTypeAdmin)
admin.site.register(DocumentType, DocumentTypeAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(MetadataGroup, MetadataGroupAdmin)
                

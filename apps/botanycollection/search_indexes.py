from haystack.indexes import SearchIndex, CharField
from haystack import site
from .models import Accession


class AccessionIndex(SearchIndex):
    text = CharField(document=True, use_template=True)

    def get_model(self):
        return Accession

    def index_queryset(self):
        """
        Used when the entire index for model is updated.
        """
        ### TODO ###
        # Ignore private/reserved etc objects
        return self.get_model().objects.all()

site.register(Accession, AccessionIndex)
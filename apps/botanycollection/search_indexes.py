from haystack import indexes
from .models import Accession


class AccessionIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Accession

    def index_queryset(self, using=None):
        """
        Used when the entire index for model is updated.
        """
        ### TODO ###
        # Ignore private/reserved etc objects
        return self.get_model().objects.all()


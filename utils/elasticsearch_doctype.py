from elasticsearch_dsl import DocType, Text, Keyword, Date, String, Nested, InnerObjectWrapper


class Tag(InnerObjectWrapper):
    """
    Definition of tag in Elasticsearch, very similar to Django ORM tables.
    """
    pass


class Photo(DocType):
    """
    Definition of photo in Elasticsearch, very similar to Django ORM tables.
    """
    text = Text(analyzer='snowball', fields={'raw': Keyword()})
    from_user = String(analyzer='snowball')
    thumbnail = Text()
    image = Text()
    tags = Nested(
        doc_class=Tag,
        properties={
            'title': Text(fields={'raw': Keyword()}),
        }
    )
    created_time = Date()

    class Meta:
        index = 'instagram'

    def add_tag(self, title):
        """
        Adding tag to photo.
        """
        self.tags.append({'title': title})
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from .elastic_serializers import Restaurant, ElasticRestaurantSerializer

@receiver(pre_save, sender=Restaurant, dispatch_uid="update_record")
def update_es_record(sender, instance, **kwargs):
    obj = ElasticRestaurantSerializer(instance)
    obj.save()

@receiver(post_delete, sender=Restaurant, dispatch_uid="delete_record")
def delete_es_record(sender, instance, *args, **kwargs):
    obj = ElasticRestaurantSerializer(instance)
    obj.delete(ignore=404)

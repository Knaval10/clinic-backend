import itertools

from django.utils.text import slugify


def generate_unique_slug(instance, field_name):
    """Generate a unique slug for the given model instance based on `field_name`."""
    base_slug = slugify(getattr(instance, field_name))
    slug = base_slug
    model = type(instance)
    for i in itertools.count(1):
        if not model.objects.filter(slug=slug).exists():
            return slug
        slug = f"{base_slug}-{i}"

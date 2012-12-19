from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from django.db.models.signals import post_delete
from mediaman.models import MediaFile


class Accession(models.Model):
    """
    An accession, including source, taxonomic, and detailed
    descriptive information.
    """
    uq_accession = models.CharField(max_length=14, blank=True, unique=True)
    material = models.CharField(max_length=50, blank=True)
    source = models.CharField(max_length=11, blank=True)
    preservation_state = models.CharField('preservation state', max_length=32, blank=True)
    family = models.CharField(max_length=50, blank=True)
    subfam = models.CharField('sub-family', max_length=50, blank=True)
    tribe = models.CharField(max_length=50, blank=True)
    species = models.CharField(max_length=50, blank=True)
    species_author = models.CharField('species author', max_length=50, blank=True)
    sspna = models.CharField('sub-species name', max_length=50, blank=True)
    sspau = models.CharField('sub-species author', max_length=50, blank=True)
    varna = models.CharField('variety name', max_length=50, blank=True)
    varau = models.CharField('variety author', max_length=50, blank=True)
    cultivar = models.CharField(max_length=50, blank=True)
    common_name = models.CharField(max_length=50, blank=True)
    biological_synonym = models.CharField(max_length=50, blank=True)
    detna = models.CharField('determination by', max_length=50, blank=True)
    detdate = models.CharField('determination date', max_length=9, blank=True)
    collector = models.CharField(max_length=50, blank=True)
    collector_serial_no = models.CharField(max_length=22, blank=True)
    collection_date = models.CharField(max_length=20, blank=True)
    source = models.CharField(max_length=67, blank=True)
    source_number = models.CharField(max_length=26, blank=True)
    id_level_flag = models.CharField(max_length=15, blank=True)
    country = models.CharField(max_length=27, blank=True)
    site_name = models.CharField(max_length=214, blank=True)
    lat_long = models.CharField('geographical coordinates', max_length=15, blank=True)
    altitude = models.CharField(max_length=14, blank=True)
    location_notes = models.CharField('location notes', max_length=162, blank=True)
    accession_notes = models.TextField(blank=True)
    related_accession = models.CharField(max_length=19, blank=True)
    weblinks = models.CharField('weblinks', max_length=20, blank=True)
    
    contributor = models.CharField(max_length=50, blank=True)
    date_contributed = models.CharField(max_length=10, blank=True)

    @models.permalink
    def get_absolute_url(self):
        return ('accession_detail', [str(self.uq_accession)])

    def __unicode__(self):
        components = (
            self.family,
            self.species)
        return ' - '.join([c for c in components if c])


class SeedFeatures(models.Model):
    """
    Detailed description of seed features

    Based on the following from Andrew Fairbairn:

    Seed/fruit type: e.g. [Caryopsis]
    Shape 3D: [small field with up to 30 characters]
    Shape 2D: [small field with up to 30 characters]
    Shape detail:  [a large field with lots of latitude for descriptions in dorsal, ventral, lateral and cross-section view]
    Size: [a range in mm typically expressed as L; B; T]
    Testa/endocarp thickness: [mm, usually a range]
    Surface outer texture/markings:
    Surface inner texture/markings: 
    Hilum details: [position, shape]
    Special features (pappus, wings etc):
    Anatomy Transverse Section: [again plenty of space required]
    Anatomy Longitudinal Sections: [plenty of space required]
    Embryo and endosperm details: [as per Martin]
    Other identification information: [A large field]
    References and links: 
    Notes: [a large field]
    Contributor: [Name of describer and date]
    """
    accession = models.OneToOneField(Accession)

    seed_type = models.CharField("seed/fruit type", max_length=50, help_text="e.g. 'Caryopsis'")
    shape_3d = models.CharField(max_length=30, blank=True)
    shape_2d = models.CharField(max_length=30, blank=True)
    shape_detail = models.TextField(blank=True, help_text="descriptions in dorsal, ventral, lateral and cross-section view")
    size = models.CharField(max_length=30, blank=True, help_text="a range in mm, typically expressed as L; B; T")
    testa_endocarp_thickness = models.CharField('testa/endocarp thickness', max_length=30, blank=True, help_text="mm, usually a range")
    surface_outer_texture = models.TextField("surface outer texture/markings", blank=True)
    surface_inner_texture = models.TextField("surface inner texture/markings", blank=True)
    hilum_details = models.CharField(max_length=30, blank=True, help_text="position, shape")
    special_features = models.TextField(blank=True, help_text="pappus, wings etc")
    anatomy_transverse_section = models.TextField(blank=True)
    anatomy_longitudinal_sections = models.TextField(blank=True)
    embryo_endosperm = models.TextField("embryo and endosperm details", blank=True, help_text="as per Martin")
    other_identification_information = models.TextField(blank=True)
    references_and_links = models.TextField(blank=True)
    notes = models.TextField(blank=True)


    class Meta:
        verbose_name_plural = "seed features"


class WoodFeatures(models.Model):
    """
    Detailed description of the features of the wood portion of the accession
    """

    accession = models.OneToOneField(Accession)

    aggregate_rays = models.CharField("aggregate rays", max_length=50, blank=True)
    australia = models.CharField("australia", max_length=50, blank=True)
    axial_canals = models.CharField("axial canals", max_length=50, blank=True)
    axial_parenchyma_arrangment = models.CharField("axial parenchyma arrangment", max_length=50, blank=True)
    axial_parenchyma_bands = models.CharField("axial parenchyma bands", max_length=50, blank=True)
    axial_parenchyma_present = models.CharField("axial parenchyma present", max_length=50, blank=True)
    cambial_variants = models.CharField("cambial variants", max_length=50, blank=True)
    common_name = models.CharField("common name", max_length=50, blank=True)
    druses = models.CharField("druses", max_length=50, blank=True)
    family = models.CharField("family", max_length=50, blank=True)
    fibre_helical_thickenings = models.CharField("fibre helical thickenings", max_length=50, blank=True)
    fibre_pits = models.CharField("fibre pits", max_length=50, blank=True)
    fibres_wall_thickeness = models.CharField("fibres wall thickeness", max_length=50, blank=True)
    fusiform_parenchyma_cells = models.CharField("fusiform parenchyma cells", max_length=50, blank=True)
    helical_thickenings = models.CharField("helical thickenings", max_length=50, blank=True)
    included_phloem = models.CharField("included phloem", max_length=80, blank=True)
    indigenous_name = models.CharField("indigenous name", max_length=80, blank=True)
    intervessels_pits_arrangment = models.CharField("intervessels pits arrangment", max_length=100, blank=True)
    intervessels_pits_size = models.CharField("intervessels pits size", max_length=100, blank=True)
    intervessels_pits_specific_shapes = models.CharField("intervessels pits specific shapes", max_length=100, blank=True)
    lactifers_tanniferous_tubes = models.CharField("lactifers tanniferous tubes", max_length=100, blank=True)
    new_caledonia = models.CharField("new caledonia", max_length=50, blank=True)
    notes = models.TextField("notes", blank=True)
    parenchyma_like_fibres_present = models.CharField("parenchyma like fibres present", max_length=100, blank=True)
    perforation_plates_types = models.CharField("perforation plates types", max_length=100, blank=True)
    prismatic_crystal = models.CharField("prismatic crystal", max_length=100, blank=True)
    radial_secretory_canals = models.CharField("radial secretory canals", max_length=50, blank=True)
    radial_tracheids_for_gymnosperms = models.CharField("radial tracheids for gymnosperms", max_length=100, blank=True)
    rays = models.CharField("rays", max_length=50, blank=True)
    rays_cellular_composition = models.CharField("rays cellular composition", max_length=150, blank=True)
    rays_height = models.CharField("rays height", max_length=50, blank=True)
    rays_sheat_cells = models.CharField("rays sheat cells", max_length=50, blank=True)
    rays_structure = models.CharField("rays structure", max_length=50, blank=True)
    rays_width = models.CharField("rays width", max_length=50, blank=True)
    reference_specimens = models.CharField("reference specimens", max_length=50, blank=True)
    silica = models.CharField("silica", max_length=50, blank=True)
    solitary_vessels_with_angular_outline = models.CharField("solitary vessels with angular outline", max_length=50, blank=True)
    species = models.CharField("species", max_length=50, blank=True)
    spetate_fibres_present = models.CharField("spetate fibres present", max_length=50, blank=True)
    storied_structure = models.CharField("storied structure", max_length=50, blank=True)
    tile_cells = models.CharField("tile cells", max_length=50, blank=True)
    turkey = models.CharField("turkey", max_length=50, blank=True)
    vascularvasicentric_tracheids_present = models.CharField("vascular-vasicentric tracheids present", max_length=100, blank=True)
    vessels = models.CharField("vessels", max_length=50, blank=True)
    vessels_arrangment = models.CharField("vessels arrangment", max_length=50, blank=True)
    vessels_deposits = models.CharField("vessels deposits", max_length=50, blank=True)
    vessels_grouping = models.CharField("vessels grouping", max_length=50, blank=True)
    vessels_porosity = models.CharField("vessels porosity", max_length=50, blank=True)
    vessels_rays_pitting = models.CharField("vessels rays pitting", max_length=50, blank=True)
    vessels_tyloses = models.CharField("vessels tyloses", max_length=50, blank=True)
    walls = models.CharField("walls", max_length=50, blank=True)

    class Meta:
        verbose_name_plural = "wood features"


class AccessionPhoto(MediaFile):
    """
    A single photo of an accession

    Should include a description
    """
    image = ThumbnailerImageField(max_length=255, upload_to='.',
        height_field='height', width_field='width')

    accession = models.ForeignKey(Accession)

    height = models.PositiveIntegerField(blank=True, null=True)
    width = models.PositiveIntegerField(blank=True, null=True)

    title = models.CharField(max_length=120, blank=True)
    description = models.TextField(max_length=100, blank=True, help_text="")

    class Meta(MediaFile.Meta):
#        unique_together = ('specimen', 'md5sum')
        pass

    def __unicode__(self):
        return self.name


def remove_delete_image_file(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(save=False)

post_delete.connect(remove_delete_image_file, sender=AccessionPhoto)

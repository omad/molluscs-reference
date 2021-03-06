from django.contrib import admin
from django.conf.urls import patterns, url
from django.conf import settings
from apps.botanycollection.models import Accession, SeedFeatures, WoodFeatures
from apps.botanycollection.models import AccessionPhoto, AccessionMetadata
from admin_views import upload_accessions_spreadsheet


class SeedFeaturesInline(admin.StackedInline):
    model = SeedFeatures


class WoodFeaturesInline(admin.StackedInline):
    model = WoodFeatures
    fieldsets = (
        ('Transverse', {
            'fields': (
                'vessels',
                'vessel_porosity',
                'tracheid_diameter',
                'vessel_grouping',
                'vessel_arrangement',
                'solitary_vessels_with_angular_outline',
                'vessels_tyloses',
                'vessels_deposits',
                'fibre_wall_thickness',
                'axial_parenchyma_present',
                'axial_parenchyma_arrangement1',
                'axial_parenchyma_arrangement2',
                'axial_parenchyma_arrangement3',
                'axial_parenchyma_arrangement4',
                'axial_parenchyma_arrangement5',
                'rays',
                'aggregate_rays',
        )}),
        ('Longitudinal', {
            'fields': (
                'intervessel_pit_arrangement',
                'intervessel_tracheid_pit_shapes',
                'intervessel_pit_size',
                'perforation_plates_types',
                'helical_thickenings',
                'fibre_helical_thickenings',
                'fibre_pits',
                'spetate_fibres_present',
                'vascularvasicentric_tracheids_present',
                'parenchyma_like_fibres_present',
                'fusiform_parenchyma_cells',
                'axial_parenchyma_bands',
                'ray_height',
                'ray_width',
                'ray_type',
                'rays_cellular_composition',
                'rays_structure',
                'rays_sheath_cells',
                'tile_cells',
                'storied_structure',
                'vessels_rays_pitting',
                'walls',
        )}),
        ('Secretory elements and cambial variants', {
            'fields': (
                'radial_tracheids_for_gymnosperms',
                'axial_canals',
                'lactifer_tanniferous_tubes',
                'radial_secretory_canals',
                'cambial_variants',
                'included_phloem',
                'druses',
                'silica',
                'prismatic_crystals',
        )}),
        ('Gymnosperm', {
            'fields': (
                'early_late_wood_transition',
                'axial_resin_canals',
                'epithelial_cells',
                'axial_tracheid_pits',
                'spiral_thickenings',
                'crassulae',
                'nodular_tangential_ray_walls',
                'early_wood_ray_pits',
                'late_wood_ray_pits',
        )}),
        ('Extra fields', {
            'fields': (
                'common_name',
                'reference_specimens',
        )})
    )


class AccessionPhotoInline(admin.StackedInline):
    model = AccessionPhoto

class AccessionMetadataInline(admin.StackedInline):
    model = AccessionMetadata

class AccessionAdmin(admin.ModelAdmin):
    def get_urls(self):
        urls = super(AccessionAdmin, self).get_urls()
        my_urls = patterns('',
            url(r'^upload/', self.admin_site.admin_view(upload_accessions_spreadsheet),
                name='upload_accessions_spreadsheet'),

        )
        return my_urls + urls
    model = Accession
    inlines = [
        SeedFeaturesInline, WoodFeaturesInline,
        AccessionPhotoInline#, AccessionMetadata
    ]

    list_display = ('uqm_accession', 'family', 'species', 'common_name', 'material')
    list_filter = ('family', )

    search_fields = ['family', 'species', 'uqm_accession'
                     'country', 'preservation_state']

    fieldsets = (
        ('Specimen details', {
            'fields': (
                'uqm_accession',
                'sample_number',
                'unique_identifier',
                'material',
                'source',
                'preservation_state',
                'related_accession',
                'accession_notes',
                'weblinks',



        )}),
        ('Classification information', {
            'fields': (
                'family',
                'subfam',
                'tribe',
                'genus',
                'species',
                'species_author',
                'sspna',
                'sspau',
                'varna',
                'varau',
                'cultivar',
                'common_name',
                'indigenous_name',
                'biological_synonym',
                'detna',
                'detdate',
                'collector',
                'collector_serial_no',
                'collection_date',
                'source_number',
                'id_level_flag',
        )}),
        ('Location', {
            'fields': (
                'country',
                'site_name',
                'lat_long',
                'altitude',
                'location_notes',
                )
        }),
    )

    class Media:
        css = {
            'all': [
                "%scss/django_admin_collapsed_inlines.css" % settings.STATIC_URL,
            ]
        }

        js = [
            "%sjs/jquery-1.8.2.min.js" % settings.STATIC_URL,
            "%sjs/django_admin_collapsed_inlines.js" % settings.STATIC_URL,
        ]



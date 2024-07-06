# __manifest__.py
{
    'name': 'Workshop BJM',
    'version': '1.0',
    'category': 'Uncategorized',
    'summary': 'Module for managing workshop data',
    'description': """Long description of module's purpose""",
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/data_konsumen.xml',
        'views/supplier_views.xml',
        'views/car_brand_form.xml',
        'views/car_brand_tree.xml',
        'views/car_brand_views.xml',
        'views/mekanik_views.xml',
        'views/kategori_produk_views.xml',
        # 'views/dashboard_views.xml',
    ],
    'installable': True,
    'application': True,
}

from store.models.category import Category
initial_data = {
        'address': 'Ck 13/14 Satti Chautra Chowk Varanasi',
        'phone_no': '918957451402',
        'email': 'sethsarees@gmail.com',
        'streetAddress': 'Ck 13/14 Satti Chautra',
        'addressLocality':'Chowk, Varanasi,',
        'addressRegion':'Uttar Pradesh',
        'postalCode':'221001',
        'categories': Category.get_all_categories(),
}
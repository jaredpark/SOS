import os

os.environ.get('FACEBOOK')

def site_settings_processor(request):
	context_dictionary = {
		'root_url': 'jpark.pythonanywhere.com',
		'admin_name': 'admin',
		'company_name': 'SOS Pool Rescue',
		'company_short': 'SOS',
		'footer_copyright': 'SurgeSite, 2015',
		'logo_file_name': 'images/new_logo.png',
		'site_email': 'saramirez48@gmail.com',
		# if email changes, update misc_pages/email.html
		'company_phone_text': '480-309-3181',
		'company_phone_link': '14803093181',
		'company_address': '3226 S Evergreen Rd Tempe, AZ 85282',
		'yelp_id': '',
		'google_plus_url': '',
		'fb_fan_page_url': '',
		'fb_app_id': '',
		'meta_content': 'Phoenix area Emergency Pool and Home Repair, Pool Cleaning, and Handyman Services',
		'navbar_link1_name': 'home',
		'navbar_link1_text': 'Home',
		'navbar_link2_name': 'pool_service',
		'navbar_link2_text': 'Weekly Service',
		'navbar_link3_name': 'pool_repair',
		'navbar_link3_text': 'Repairs',
		'navbar_link4_name': 'all_services',
		'navbar_link4_text': 'All Services',
		'navbar_link5_name': 'about',
		'navbar_link5_text': 'About',
		'navbar_link6_name': 'contact',
		'navbar_link6_text': 'Contact',
		# 'sublink1_name': 'pool_repair',
		# 'sublink1_text': 'Pool Repair',
		# 'sublink2_name': 'pool_service',
		# 'sublink2_text': 'Pool Service',
		# 'sublink3_name': 'pool_service',
		# 'sublink3_text': 'Handyman',
	}
	return(context_dictionary)
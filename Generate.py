import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import uuid

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Generate 50 unique applicant IDs
applicant_ids = [f'APP{str(i).zfill(3)}' for i in range(1, 51)]

# 1. Applicant Basic Information
applicant_data = []
for i, app_id in enumerate(applicant_ids):
    applicant_data.append({
        'applicant_id': app_id,
        'full_name': f'Applicant {i+1}',
        'date_of_birth': (datetime.now() - timedelta(days=random.randint(7300, 14600))).strftime('%Y-%m-%d'),
        'gender': random.choice(['Male', 'Female']),
        'marital_status': random.choice(['Single', 'Married', 'Divorced']),
        'pan_number': f'ABCDE{random.randint(1000, 9999)}F',
        'aadhaar_number': f'{random.randint(1000, 9999)} {random.randint(1000, 9999)} {random.randint(1000, 9999)}',
        'phone_number': f'9{random.randint(100000000, 999999999)}',
        'email': f'applicant{i+1}@example.com',
        'education': random.choice(['Graduate', 'Post Graduate', 'Doctorate', 'Diploma']),
        'father_name': f'Father of Applicant {i+1}',
        'mother_name': f'Mother of Applicant {i+1}',
        'spouse_name': f'Spouse of Applicant {i+1}' if random.choice([True, False]) else '',
        'created_date': (datetime.now() - timedelta(days=random.randint(1, 30))).strftime('%Y-%m-%d'),
        'updated_date': datetime.now().strftime('%Y-%m-%d'),
        'is_active': random.choice([True, False]),
        'income_range': random.choice(['0-5L', '5-10L', '10-20L', '20-50L', '50L+']),
        'cibil_score_range': random.choice(['300-500', '500-600', '600-700', '700-800', '800-900']),
        'employment_type': random.choice(['Salaried', 'Self-Employed', 'Business', 'Professional']),
        'number_of_dependents': random.randint(0, 5),
        'nationality': 'Indian',
        'source_of_lead': random.choice(['Website', 'Referral', 'Bank Branch', 'Marketing Campaign']),
        'marketing_consent': random.choice([True, False]),
        'communication_preference': random.choice(['Email', 'SMS', 'WhatsApp', 'Phone']),
        'applicant_category': random.choice(['New', 'Existing', 'Premium'])
    })

df_applicant = pd.DataFrame(applicant_data)

# 2. Address Information
address_data = []
for app_id in applicant_ids:
    for addr_type in ['Residential', 'Business']:
        address_data.append({
            'address_id': f'ADD{len(address_data)+1:03d}',
            'applicant_id': app_id,
            'application_id': f'APPN{random.randint(1, 30):03d}',
            'address_type': addr_type,
            'flat_number': f'{random.choice(["A", "B", "C"])}-{random.randint(1, 50)}',
            'building_number': f'Building {random.randint(1, 20)}',
            'society_name': random.choice(['Green Valley', 'Royal Palms', 'Sunrise Apartments', '']),
            'gated_community': random.choice([True, False]),
            'street': f'{random.choice(["MG Road", "Park Street", "Church Street"])}',
            'area': random.choice(['Koramangala', 'Bandra', 'Pune City', 'Gurgaon Sector']),
            'landmark': random.choice(['Near Metro', 'Opposite Mall', 'Next to Hospital']),
            'city': random.choice(['Mumbai', 'Delhi', 'Bangalore', 'Chennai', 'Hyderabad']),
            'state': random.choice(['Maharashtra', 'Delhi', 'Karnataka', 'Tamil Nadu', 'Telangana']),
            'pincode': random.randint(400000, 799999),
            'state_code': random.choice(['MH', 'DL', 'KA', 'TN', 'TS']),
            'ownership_status': random.choice(['Owned', 'Rented', 'Leased']),
            'landlord_name': f'Landlord {random.randint(1, 100)}',
            'owned_by': f'Owner {random.randint(1, 100)}',
            'years_in_address': random.randint(1, 10),
            'months_in_address': random.randint(0, 11),
            'old_address': f'Old address of {app_id}',
            'years_in_old_address': random.randint(0, 5),
            'months_in_old_address': random.randint(0, 11),
            'same_as_residence': random.choice([True, False]),
            'same_as_permanent': random.choice([True, False]),
            'same_as_applicant': random.choice([True, False]),
            'address_verified': random.choice([True, False]),
            'address_proof_type': random.choice(['Aadhaar', 'Utility Bill', 'Passport']),
            'monthly_rent': random.choice([0, 5000, 10000, 15000, 20000])
        })

df_address = pd.DataFrame(address_data)

# 3. Business Details (for self-employed applicants)
business_data = []
for app_id in applicant_ids:
    if random.choice([True, False]):  # 50% chance of being business
        business_data.append({
            'verification_id': f'VER{len(business_data)+1:03d}',
            'applicant_id': app_id,
            'application_id': f'APPN{random.randint(1, 30):03d}',
            'business_cluster_type': random.choice(['MSME Services', 'Manufacturing', 'E-Commerce', 'Retail']),
            'business_domain': random.choice(['Healthcare', 'Education', 'Construction', 'IT Services']),
            'business_type': random.choice(['Pvt Ltd.', 'LLP', 'Partnership', 'Sole Proprietorship']),
            'business_company_name': f'{random.choice(["Tech", "Global", "Premium", "Smart"])} Solutions Pvt Ltd',
            'business_company_pan': f'ABCDE{random.randint(1000, 9999)}F',
            'gstin': f'{random.randint(10, 99)}ABCDE{random.randint(1000, 9999)}F{random.randint(1, 9)}Z{random.randint(1, 9)}',
            'incorporation_date': (datetime.now() - timedelta(days=random.randint(365, 3650))).strftime('%Y-%m-%d'),
            'business_status': random.choice(['Active', 'Inactive']),
            'annual_turnover': random.randint(1000000, 50000000),
            'business_contact_number': f'9{random.randint(100000000, 999999999)}',
            'registration_number': f'REG{random.randint(10000, 99999)}',
            'business_emailid': f'business{random.randint(1, 100)}@company.com',
            'net_profit': random.randint(100000, 5000000),
            'employee_count': random.randint(1, 100),
            'ownership_type': random.choice(['Family owned', 'Private owned', 'Public owned']),
            'years_in_operation': random.randint(1, 20),
            'last_funded_date': (datetime.now() - timedelta(days=random.randint(30, 365))).strftime('%Y-%m-%d') if random.choice([True, False]) else '',
            'has_existing_loans': random.choice([True, False]),
            'number_of_branches': random.randint(1, 5),
            'existing_emi_amount': random.randint(10000, 100000) if random.choice([True, False]) else 0,
            'business_credit_score': random.randint(300, 900)
        })

df_business = pd.DataFrame(business_data)

# Continue this pattern for all 20 tables...

# Save to Excel
with pd.ExcelWriter('eKYC_Dummy_Data.xlsx', engine='openpyxl') as writer:
    df_applicant.to_excel(writer, sheet_name='Applicant', index=False)
    df_address.to_excel(writer, sheet_name='Address', index=False)
    df_business.to_excel(writer, sheet_name='Business', index=False)
    # Add all other dataframes...
    
print("Dataset generated successfully!")

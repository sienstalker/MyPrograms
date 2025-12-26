import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import os

# Create output directory
output_dir = "ekyc_dummy_data"
os.makedirs(output_dir, exist_ok=True)

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Indian names for realistic data
first_names_male = ['Rajesh', 'Amit', 'Vikram', 'Sanjay', 'Rahul', 'Kumar', 'Arun', 'Deepak', 'Nikhil', 'Prakash']
first_names_female = ['Priya', 'Sunita', 'Anjali', 'Meera', 'Sneha', 'Pooja', 'Ritu', 'Neha', 'Shweta', 'Kavita']
last_names = ['Sharma', 'Verma', 'Patel', 'Reddy', 'Singh', 'Kumar', 'Gupta', 'Jain', 'Malhotra', 'Choudhury']

cities_states = [
    ('Mumbai', 'Maharashtra', 'MH'),
    ('Delhi', 'Delhi', 'DL'),
    ('Bangalore', 'Karnataka', 'KA'),
    ('Chennai', 'Tamil Nadu', 'TN'),
    ('Hyderabad', 'Telangana', 'TS'),
    ('Kolkata', 'West Bengal', 'WB'),
    ('Pune', 'Maharashtra', 'MH'),
    ('Ahmedabad', 'Gujarat', 'GJ')
]

banks = ['SBI', 'HDFC', 'ICICI', 'Axis', 'Kotak', 'PNB', 'Yes Bank']

# Generate 50 unique applicant IDs
applicant_ids = [f'APP{str(i).zfill(3)}' for i in range(1, 51)]

# 1. Applicant Basic Information
print("Generating Applicant data...")
applicant_data = []
for i, app_id in enumerate(applicant_ids):
    gender = random.choice(['Male', 'Female'])
    if gender == 'Male':
        first_name = random.choice(first_names_male)
    else:
        first_name = random.choice(first_names_female)
    last_name = random.choice(last_names)
    
    applicant_data.append({
        'applicant_id': app_id,
        'full_name': f'{first_name} {last_name}',
        'date_of_birth': (datetime.now() - timedelta(days=random.randint(7300, 14600))).strftime('%Y-%m-%d'),
        'gender': gender,
        'marital_status': random.choice(['Single', 'Married', 'Divorced']),
        'pan_number': f'ABCDE{random.randint(1000, 9999)}F',
        'aadhaar_number': f'{random.randint(1000, 9999)}{random.randint(1000, 9999)}{random.randint(1000, 9999)}',
        'phone_number': f'9{random.randint(100000000, 999999999)}',
        'email': f'{first_name.lower()}.{last_name.lower()}{random.randint(1, 99)}@example.com',
        'education': random.choice(['Graduate', 'Post Graduate', 'Doctorate', 'Diploma']),
        'father_name': f'Mr. {random.choice(first_names_male)} {last_name}',
        'mother_name': f'Mrs. {random.choice(first_names_female)} {last_name}',
        'spouse_name': f'{random.choice(first_names_female)} {last_name}' if gender == 'Male' and random.choice([True, False]) else '',
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
df_applicant.to_csv(f'{output_dir}/1_applicant.csv', index=False)

# 2. Generate Application IDs
application_ids = [f'APPN{str(i).zfill(3)}' for i in range(1, 31)]

# 2. Address Information
print("Generating Address data...")
address_data = []
for i, app_id in enumerate(applicant_ids):
    for addr_type in ['Residential', 'Business']:
        city, state, state_code = random.choice(cities_states)
        address_data.append({
            'address_id': f'ADD{len(address_data)+1:03d}',
            'applicant_id': app_id,
            'application_id': random.choice(application_ids) if random.choice([True, False]) else '',
            'address_type': addr_type,
            'flat_number': f'{random.choice(["A", "B", "C", "D", "E"])}-{random.randint(1, 50)}',
            'building_number': f'Building {random.randint(1, 20)}',
            'society_name': random.choice(['Green Valley', 'Royal Palms', 'Sunrise Apartments', 'Lake View', 'Garden Enclave', '']),
            'gated_community': random.choice([True, False]),
            'street': f'{random.choice(["MG Road", "Park Street", "Church Street", "Main Road", "Gandhi Road"])}',
            'area': random.choice(['Koramangala', 'Bandra', 'Andheri', 'Connaught Place', 'Jayanagar']),
            'landmark': random.choice(['Near Metro Station', 'Opposite Mall', 'Next to Hospital', 'Behind Police Station']),
            'city': city,
            'state': state,
            'pincode': random.randint(400000, 799999),
            'state_code': state_code,
            'ownership_status': random.choice(['Owned', 'Rented', 'Leased']),
            'landlord_name': f'Mr. {random.choice(first_names_male)} {random.choice(last_names)}' if random.choice([True, False]) else '',
            'owned_by': f'Mr. {random.choice(first_names_male)} {random.choice(last_names)}',
            'years_in_address': random.randint(1, 10),
            'months_in_address': random.randint(0, 11),
            'old_address': f'Old address in {random.choice(cities_states)[0]}',
            'years_in_old_address': random.randint(0, 5),
            'months_in_old_address': random.randint(0, 11),
            'same_as_residence': random.choice([True, False]),
            'same_as_permanent': random.choice([True, False]),
            'same_as_applicant': random.choice([True, False]),
            'address_verified': random.choice([True, False]),
            'address_proof_type': random.choice(['Aadhaar', 'Utility Bill', 'Passport', 'Driving License']),
            'monthly_rent': random.choice([0, 5000, 10000, 15000, 20000, 25000])
        })

df_address = pd.DataFrame(address_data)
df_address.to_csv(f'{output_dir}/2_address.csv', index=False)

# 3. Business Details
print("Generating Business data...")
business_data = []
for i, app_id in enumerate(applicant_ids):
    if random.choice([True, False]):  # 50% chance of being business
        business_data.append({
            'verification_id': f'VER{len(business_data)+1:03d}',
            'applicant_id': app_id,
            'application_id': random.choice(application_ids),
            'business_cluster_type': random.choice(['MSME Services', 'Manufacturing', 'E-Commerce', 'Retail', 'IT Services']),
            'business_domain': random.choice(['Healthcare', 'Education', 'Construction', 'IT Services', 'Agriculture']),
            'business_type': random.choice(['Pvt Ltd.', 'LLP', 'Partnership', 'Sole Proprietorship']),
            'business_company_name': f'{random.choice(["Tech", "Global", "Premium", "Smart", "Innovative"])} Solutions Pvt Ltd',
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
df_business.to_csv(f'{output_dir}/3_business.csv', index=False)

# 4. Employment Details (Raw)
print("Generating Employment data...")
employment_data = []
for i, app_id in enumerate(applicant_ids):
    employment_data.append({
        'employment_id': f'EMP{len(employment_data)+1:03d}',
        'applicant_id': app_id,
        'application_id': random.choice(application_ids),
        'employment_type': random.choice(['Full Time', 'Part Time', 'Contract', 'Internship', 'Unemployed']),
        'employer_name': random.choice(['Infosys', 'TCS', 'Wipro', 'HCL', 'Tech Mahindra', 'Reliance', 'Tata']),
        'employer_address': f'Office in {random.choice(cities_states)[0]}',
        'employer_ph_no': f'022{random.randint(1000000, 9999999)}',
        'employee_emailid': f'employee{random.randint(1, 1000)}@company.com',
        'designation': random.choice(['Software Engineer', 'Manager', 'Analyst', 'Consultant', 'Director']),
        'department': random.choice(['IT', 'Finance', 'HR', 'Marketing', 'Operations']),
        'start_date': (datetime.now() - timedelta(days=random.randint(365, 3650))).strftime('%Y-%m-%d'),
        'employment_tenure_years': random.randint(1, 10),
        'employment_tenure_months': random.randint(0, 11),
        'monthly_income': random.choice([30000, 50000, 75000, 100000, 150000, 200000])
    })

df_employment = pd.DataFrame(employment_data)
df_employment.to_csv(f'{output_dir}/4_employment.csv', index=False)

# 5. Application Basic Info
print("Generating Application data...")
application_data = []
for i, app_id in enumerate(applicant_ids[:30]):  # 30 applications
    application_data.append({
        'application_id': application_ids[i],
        'applicant_id': app_id,
        'product': random.choice(['Home Loan', 'Personal Loan', 'Car Loan', 'Education Loan', 'Business Loan']),
        'branch_id': f'BR{random.randint(1, 50):03d}',
        'loan_amount': random.choice([500000, 1000000, 1500000, 2000000, 3000000, 5000000]),
        'loan_roi': round(random.uniform(7.5, 15.0), 2),
        'loan_tenure': random.choice([12, 24, 36, 60, 84, 120, 240]),
        'servicing_la': f'LA{random.randint(1, 20):03d}',
        'application_date': (datetime.now() - timedelta(days=random.randint(1, 60))).strftime('%Y-%m-%d %H:%M:%S'),
        'app_updated_date_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'app_status': random.choice(['Pending', 'Approved', 'Rejected', 'Processing', 'Documentation']),
        'loan_type': random.choice(['Secured', 'Unsecured']),
        'is_ai_audited': random.choice([True, False]),
        'ai_audit_status': random.choice(['Pending', 'Completed', 'Failed'])
    })

df_application = pd.DataFrame(application_data)
df_application.to_csv(f'{output_dir}/5_application.csv', index=False)

# 6. Loan Charges
print("Generating Loan Charges data...")
loan_charges_data = []
for i, app_id in enumerate(application_ids[:20]):  # Charges for 20 applications
    for charge_type in ['Processing Fee', 'Stamp Duty', 'Legal Charges', 'Insurance']:
        amount = random.choice([1000, 2500, 5000, 10000, 15000])
        gst_amount = amount * 0.18 if random.choice([True, False]) else 0
        
        loan_charges_data.append({
            'loan_charge_id': f'CHG{len(loan_charges_data)+1:03d}',
            'application_id': app_id,
            'charge_id': f'C{random.randint(100, 999)}',
            'charge_type': charge_type,
            'amount_value': amount,
            'gst_applicable': gst_amount > 0,
            'gst_amount': round(gst_amount, 2),
            'total_payable': round(amount + gst_amount, 2),
            'is_refundable': random.choice([True, False]),
            'charge_status': random.choice(['Pending', 'Collected', 'Waived']),
            'payment_mode': random.choice(['UPI', 'Credit Card', 'Debit Card', 'Net Banking']),
            'collected_on': (datetime.now() - timedelta(days=random.randint(1, 30))).strftime('%Y-%m-%d') if random.choice([True, False]) else '',
            'collected_by': f'EMP{random.randint(1, 20):03d}',
            'applicable_stage': random.choice(['Application', 'Approval', 'Disbursement']),
            'charge_due_date': (datetime.now() + timedelta(days=random.randint(7, 30))).strftime('%Y-%m-%d'),
            'payment_ref_id': f'REF{random.randint(10000, 99999)}' if random.choice([True, False]) else '',
            'waiver_applicable': random.choice([True, False]),
            'waiver_approved_by': f'EMP{random.randint(1, 20):03d}' if random.choice([True, False]) else '',
            'receipt_id': f'RCPT{random.randint(1000, 9999)}' if random.choice([True, False]) else '',
            'penalty_applicable': random.choice([True, False])
        })

df_loan_charges = pd.DataFrame(loan_charges_data)
df_loan_charges.to_csv(f'{output_dir}/6_loan_charges.csv', index=False)

# 7. Banking Information
print("Generating Banking data...")
banking_data = []
for i, app_id in enumerate(applicant_ids[:40]):  # Banking for 40 applicants
    banking_data.append({
        'application_id': random.choice(application_ids),
        'applicant_id': app_id,
        'is_disb_account': random.choice([True, False]),
        'account_type': random.choice(['Savings', 'Current']),
        'account_holder_name': applicant_data[i]['full_name'],
        'ifsc_code': f'{random.choice(["SBIN", "HDFC", "ICIC", "UTIB", "KKBK"])}00{random.randint(1000, 9999)}',
        'micr_code': f'{random.randint(100000, 999999)}',
        'bank_name': random.choice(banks),
        'branch_name': f'{random.choice(banks)} {random.choice(cities_states)[0]} Branch',
        'account_number': f'{random.randint(1000000000, 9999999999)}',
        'confirm_account_number': f'{random.randint(1000000000, 9999999999)}',
        'acc_linked_mobile': random.choice([True, False]),
        'acc_status': random.choice(['Active', 'Inactive', 'Dormant']),
        'acc_opened_at': (datetime.now() - timedelta(days=random.randint(365, 3650))).strftime('%Y-%m-%d'),
        'consent_captured': random.choice([True, False])
    })

df_banking = pd.DataFrame(banking_data)
df_banking.to_csv(f'{output_dir}/7_banking.csv', index=False)

# 8. Documents
print("Generating Documents data...")
documents_data = []
for i, app_id in enumerate(applicant_ids):
    for doc_type in ['PAN Card', 'Aadhaar Card', 'Address Proof', 'Income Proof', 'Bank Statement']:
        documents_data.append({
            'document_id': f'DOC{len(documents_data)+1:03d}',
            'application_id': random.choice(application_ids),
            'applicant_id': app_id,
            'document_type': doc_type,
            'document_link': f'https://storage.blob.core.windows.net/documents/{app_id}_{doc_type.replace(" ", "_")}.pdf',
            'uploaded_by': f'EMP{random.randint(1, 10):03d}',
            'uploaded_date_time': (datetime.now() - timedelta(days=random.randint(1, 30))).strftime('%Y-%m-%d %H:%M:%S'),
            'verified_by': f'EMP{random.randint(11, 20):03d}' if random.choice([True, False]) else '',
            'verified_date_time': (datetime.now() - timedelta(days=random.randint(1, 15))).strftime('%Y-%m-%d %H:%M:%S') if random.choice([True, False]) else '',
            'document_name': doc_type,
            'document_status': random.choice(['Verified', 'Pending', 'Rejected']),
            'rejection_reason': random.choice(['Blurry', 'Expired', 'Mismatch', '']) if random.choice([True, False]) else '',
            'file_size': random.randint(100000, 5000000),
            'file_type': 'PDF',
            'ocr_confidence_score': round(random.uniform(0.7, 0.99), 2),
            'blob_storage_path': f'/documents/{app_id}/{doc_type.replace(" ", "_")}.pdf'
        })

df_documents = pd.DataFrame(documents_data)
df_documents.to_csv(f'{output_dir}/8_documents.csv', index=False)

# 9. Risk Assessment
print("Generating Risk Assessment data...")
risk_data = []
for i, app_id in enumerate(application_ids):
    cibil_score = random.randint(300, 900)
    risk_grade = 'Low' if cibil_score > 750 else 'Medium' if cibil_score > 600 else 'High'
    
    risk_data.append({
        'risk_id': f'RISK{len(risk_data)+1:03d}',
        'application_id': app_id,
        'risk_grade': risk_grade,
        'cibil_score': cibil_score,
        'debt_to_income_ratio': round(random.uniform(0.1, 0.8), 2),
        'existing_loan_count': random.randint(0, 5),
        'existing_emi_total': random.randint(0, 50000),
        'employment_stability_years': random.randint(1, 15),
        'risk_flags': random.choice(['High DTI', 'Low CIBIL', 'Multiple Loans', 'New Employment', '']),
        'is_high_risk': risk_grade == 'High',
        'risk_assessment_date': (datetime.now() - timedelta(days=random.randint(1, 30))).strftime('%Y-%m-%d'),
        'monthly_income': random.choice([30000, 50000, 75000, 100000, 150000]),
        'employment_type': random.choice(['Salaried', 'Self-Employed']),
        'credit_life_insurance': random.choice([True, False]),
        'assessment_done_by': f'EMP{random.randint(1, 20):03d}',
        'ai_model_version': 'gpt-4o-2024-05-13'
    })

df_risk = pd.DataFrame(risk_data)
df_risk.to_csv(f'{output_dir}/9_risk_assessment.csv', index=False)

# 10. Verification Type
print("Generating Verification data...")
verification_data = []
for i in range(50):  # 50 verifications
    verification_data.append({
        'verification_id': f'VER{len(verification_data)+1:03d}',
        'applicant_id': random.choice(applicant_ids),
        'application_id': random.choice(application_ids),
        'verification_type': random.choice(['House', 'Business', 'Employment', 'Address']),
        'verified_by': f'EMP{random.randint(1, 20):03d}',
        'verification_date_time': (datetime.now() - timedelta(days=random.randint(1, 30))).strftime('%Y-%m-%d %H:%M:%S'),
        'verification_status': random.choice(['Completed', 'Pending', 'Failed']),
        'remarks': random.choice(['All documents verified', 'Address mismatch', 'Employment confirmed', ''])
    })

df_verification = pd.DataFrame(verification_data)
df_verification.to_csv(f'{output_dir}/10_verification.csv', index=False)

# Generate remaining tables with similar pattern
print("Generating remaining tables...")

# 11. Verification Details (sample 20 rows)
verification_details_data = []
for i in range(20):
    verification_details_data.append({
        'verification_id': f'VER{random.randint(1, 50):03d}',
        'applicant_id': random.choice(applicant_ids),
        'application_id': random.choice(application_ids),
        'contact_person_name': random.choice(first_names_male + first_names_female) + ' ' + random.choice(last_names),
        'contact_person_number': f'9{random.randint(100000000, 999999999)}',
        'ownership_status': random.choice(['Owned', 'Rented', 'Leased']),
        'flat_number': f'{random.choice(["A", "B"])}-{random.randint(1, 30)}',
        'building_number': f'Building {random.randint(1, 10)}',
        'society_name': random.choice(['Sunrise', 'Green Valley', 'Royal']),
        'gated_community': random.choice([True, False]),
        'street': random.choice(['MG Road', 'Park Street']),
        'area': random.choice(['Koramangala', 'Bandra']),
        'landmark': 'Near Metro Station',
        'city': random.choice(cities_states)[0],
        'state': random.choice(cities_states)[1],
        'pincode': random.randint(400000, 799999),
        'state_code': random.choice(['MH', 'DL', 'KA']),
        'landlord_name': f'Mr. {random.choice(first_names_male)} {random.choice(last_names)}',
        'owned_by': f'Mr. {random.choice(first_names_male)} {random.choice(last_names)}',
        'years_in_address': random.randint(1, 10),
        'months_in_address': random.randint(0, 11),
        'monthly_rent': random.randint(0, 25000),
        'no_of_children': random.randint(0, 3),
        'child_name_1': random.choice(first_names_male + first_names_female) if random.choice([True, False]) else '',
        'child_age_1': random.randint(1, 18) if random.choice([True, False]) else 0,
        'child_gender_1': random.choice(['Male', 'Female']) if random.choice([True, False]) else '',
        'child_name_2': random.choice(first_names_male + first_names_female) if random.choice([True, False]) else '',
        'child_age_2': random.randint(1, 18) if random.choice([True, False]) else 0,
        'child_gender_2': random.choice(['Male', 'Female']) if random.choice([True, False]) else '',
        'property_title_number': f'TITLE{random.randint(10000, 99999)}',
        'property_size': random.randint(500, 3000),
        'water_supply_source': random.choice(['Municipal', 'Borewell', 'Tanker']),
        'gas_supply_source': random.choice(['Pipeline', 'Cylinder']),
        'sewage_system': random.choice(['Septic Tank', 'Municipal']),
        'electricity_connection': random.choice(['Metered', 'Non-metered']),
        'electricity_bill_applicant': random.choice([True, False]),
        'property_insurance': random.choice([True, False]),
        'property_tax_current': random.randint(1000, 20000),
        'flood_zone': random.choice([True, False]),
        'legal_clearance': random.choice([True, False]),
        'four_wheeler': random.choice([True, False]),
        'two_wheeler': random.choice([True, False]),
        'number_of_floors': random.randint(1, 5),
        'number_of_rooms': random.randint(1, 6),
        'availability_of_basic_amenities': random.choice([True, False]),
        'condition_of_house': random.choice(['Good', 'Average', 'Poor']),
        'marriage_within_one_year': random.choice([True, False]),
        'total_members_staying': random.randint(1, 6),
        'bed_ridden_members': random.randint(0, 2),
        'house_construction_status': random.choice(['Complete', 'Under Construction']),
        'house_renovation_history': random.choice([True, False]),
        'mortgage_status': random.choice([True, False]),
        'health_insurance': random.choice([True, False]),
        'life_insurance': random.choice([True, False]),
        'property_tax_paid': random.choice([True, False]),
        'neighbour_feedback': random.choice(['Good', 'Average', 'Not Known'])
    })

df_verification_details = pd.DataFrame(verification_details_data)
df_verification_details.to_csv(f'{output_dir}/11_verification_details.csv', index=False)

# 12. Lead Tracking
print("Generating Lead Tracking data...")
lead_data = []
for i in range(30):
    lead_data.append({
        'lead_id': f'LEAD{random.randint(1000, 9999)}',
        'curr_stage': random.choice(['New', 'Documentation', 'Verification', 'Approval', 'Disbursed']),
        'prev_stage': random.choice(['New', 'Documentation', 'Verification']),
        'next_stage': random.choice(['Verification', 'Approval', 'Disbursed']),
        'is_stuck': random.choice([True, False]),
        'lead_age': random.randint(1, 90),
        'is_error': random.choice([True, False]),
        'is_dev': random.choice([True, False]),
        'is_trash': random.choice([True, False]),
        'is_sanctioned': random.choice([True, False])
    })

df_lead = pd.DataFrame(lead_data)
df_lead.to_csv(f'{output_dir}/12_lead_tracking.csv', index=False)

print(f"\n✅ Data generation complete! Check the '{output_dir}' folder for all CSV files.")
print("Files generated:")
for i in range(1, 13):
    print(f"  {i}. {output_dir}/{['applicant','address','business','employment','application','loan_charges','banking','documents','risk_assessment','verification','verification_details','lead_tracking'][i-1]}.csv")

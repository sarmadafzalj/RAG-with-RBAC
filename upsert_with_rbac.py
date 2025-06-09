from pinecone.grpc import PineconeGRPC as Pinecone
from openai import OpenAI
from dotenv import load_dotenv
from uuid import uuid4
import os
load_dotenv()

#pinecone client
pc = Pinecone(api_key=os.getenv("pineconekey"))
index = pc.Index("ragwithrbac")
#openai client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

#data to upsert
text_financial_report = """

📘 1. Financial Report – Dummy Company: "NimbusTech Inc."
Overview:
NimbusTech Inc. is a fictional mid-sized technology solutions company operating across North America, Europe, and Asia-Pacific. This financial report covers a full fiscal year.

Key Sections:
📅 Fiscal Year: 2024
🏢 Regions: North America, Europe, Asia-Pacific
📦 Business Units:
Cloud Services

Software Products

IT Consulting

🔢 Revenue Overview
Quarter	Region	Business Unit	Revenue ($M)	COGS ($M)	Gross Profit ($M)	Margin %
Q1	North America	Cloud Services	15.2	7.3	7.9	52.0%
Q2	Europe	Software Products	12.5	5.6	6.9	55.2%
Q3	Asia-Pacific	IT Consulting	9.1	4.5	4.6	50.5%
Q4	North America	Software Products	13.7	6.0	7.7	56.2%

📉 Operating Expenses Breakdown (Annual)
Category	Total ($M)
Salaries & Wages	22.8
Marketing	5.4
R&D	7.2
Travel	2.1
IT Infrastructure	4.9
Legal/Compliance	1.3

💰 Key Financial Ratios
EBITDA Margin: 24.3%

Net Profit Margin: 15.2%

Debt-to-Equity Ratio: 0.43

Current Ratio: 1.75

🧾 Balance Sheet Summary (Q4 End)
Assets	Amount ($M)	Liabilities	Amount ($M)
Cash & Equivalents	18.2	Accounts Payable	7.1
Accounts Receivable	12.7	Short-Term Debt	6.4
Property & Equipment	34.5	Long-Term Liabilities	14.0
Intangible Assets	9.8		
Total Assets	75.2	Total Liabilities	27.5
"""

text_HR_dataset = """
📗 2. HR Report – Dummy Company: "NimbusTech Inc."
Overview:
This HR dataset models detailed personnel data for 200 employees at NimbusTech Inc., spanning demographics, roles, performance, and engagement.

👥 Employee Demographics
Attribute	Distribution
Gender	58% Male, 42% Female
Age Range	21–60 (Median: 34)
Education	72% Bachelor's, 18% Master's, 10% PhD
Marital Status	48% Married, 52% Single

🧑‍💼 Role Distribution
Department	Headcount	Avg. Tenure (yrs)	Avg. Salary ($)
Engineering	75	4.3	93,000
Sales	30	3.1	76,000
HR & Admin	15	5.2	68,000
Finance	20	4.8	82,000
IT Support	10	2.7	60,000
Product Management	20	3.6	105,000
Marketing	30	3.2	72,000

📈 Performance Metrics
Rating	Employees	Notes
Exceeds Expectation (5)	42	Considered for promotion
Meets Expectation (4)	110	Core performers
Below Expectation (3)	38	Needs targeted development
Poor (1–2)	10	At risk of exit or improvement plan

📊 Engagement & Retention
Voluntary Turnover (YTD): 7.5%

Involuntary Exits: 3%

Internal Mobility Rate: 12%

Avg. Training Hours/Employee: 24

ESAT (Employee Satisfaction): 81%

"""

data_list = {"finance" : text_financial_report, "hr" : text_HR_dataset}

for k, v in data_list.items():
    try:
        response = client.embeddings.create(
        input=v,
        model="text-embedding-3-large"
        )

        embeddigs = response.data[0].embedding

        index.upsert(
        vectors=[
            {
            "id": str(uuid4()), 
            "values": embeddigs, 
            "metadata": {
                "role": k,
                "text": v}
                }
        ],
        namespace="demo"
        )
    except Exception as e:
        print(e)

        
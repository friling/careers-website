
from flask import Flask, render_template, request, send_file
import pandas as pd
import io
import openpyxl

app = Flask(__name__)

def process_excel(file):
    # Read the Excel file
    df = pd.read_excel(file, sheet_name='English Version', header=7)
    
    # Extract required columns
    df = df[['Part #', 'Suggested Trade Price']]
    
    # Rename columns
    df.columns = ['Prod', 'Base Price']
    
    # Ensure Prod is a string and truncate to 24 characters
    df['Prod'] = df['Prod'].astype(str).str[:24]
    
    # Convert Base Price to the required format
    df['Base Price'] = df['Base Price'].apply(lambda x: f"{x:012.5f}")
    
    # Add placeholder columns
    df['List Price'] = '000000000.00000'
    df['Replacement Cost'] = '000000000.00000'
    df['Last Foreign Cost'] = '000000000.00000'
    
    return df

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename.endswith(('.xlsx', '.xls')):
            df = process_excel(file)
            
            # Create a BytesIO object to store the CSV
            output = io.BytesIO()
            df.to_csv(output, index=False, sep=',', encoding='utf-8')
            output.seek(0)
            
            return send_file(
                output,
                as_attachment=True,
                download_name='output.csv',
                mimetype='text/csv'
            )
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
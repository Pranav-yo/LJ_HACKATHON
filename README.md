<h1>💰 AI Finance Assistant (Gemini 2.0)</h1>

<p>
An <b>AI-powered personal finance assistant</b> built with 
<b>Streamlit</b> and <b>Google Gemini 2.0 Flash</b>, designed to help users understand 
and manage their financial data in real time.  
</p>

<h2>🚀 Features</h2>
<ul>
  <li><b>AI-Powered Chat</b>: Ask natural language questions about your money.</li>
  <li><b>Finance Data Integration</b>: Uses structured financial data (<code>finance.json</code>) for personalized insights.</li>
  <li><b>Data Permissions</b>: Toggle access to assets, liabilities, transactions, EPF, credit score, and investments.</li>
  <li><b>Interactive UI</b>: Built with Streamlit for a clean and responsive experience.</li>
  <li><b>Secure & Configurable</b>: Gemini API key required for AI responses.</li>
</ul>

<h2>📂 Project Structure</h2>
<pre>
├── App.py          # Streamlit application
├── finance.json    # Sample financial dataset
├── README.md       # Project documentation
</pre>

<h2>⚙️ Installation & Setup</h2>

<h3>1. Clone Repository</h3>
<pre><code>git clone https://github.com/your-username/ai-finance-assistant.git
cd ai-finance-assistant
</code></pre>

<h3>2. Create Virtual Environment</h3>
<pre><code>python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
</code></pre>

<h3>3. Install Dependencies</h3>
<pre><code>pip install -r requirements.txt
</code></pre>

<p><i>(Create a <code>requirements.txt</code> with the following:)</i></p>
<pre><code>streamlit
google-generativeai
</code></pre>

<h3>4. Add Your Gemini API Key</h3>
<p>In <b>App.py</b>, replace the placeholder with your API key:</p>
<pre><code>API_KEY = "YOUR_GEMINI_API_KEY"
</code></pre>

<h3>5. Run the Application</h3>
<pre><code>streamlit run App.py
</code></pre>

<h2>📊 Example Financial Data (<code>finance.json</code>)</h2>
<pre><code>{
  "assets": {
    "cash": 50000,
    "bank_balance": 200000,
    "property": 280000
  },
  "liabilities": {
    "loans": 100000,
    "credit_card_debt": 20000
  },
  "transactions": [
    { "date": "2025-08-01", "type": "income", "amount": 50000 },
    { "date": "2025-08-05", "type": "expense", "amount": 2000 }
  ],
  "epf": {
    "contributions": 100000,
    "employer_match": 50000,
    "current_balance": 150000
  },
  "credit_score": { "score": 750, "rating": "Good" },
  "investments": { "stocks": 100000, "mutual_funds": 80000, "bonds": 50000 }
}
</code></pre>

<h2>🖼️ Screenshots</h2>
<p><i>(Add screenshots of the Streamlit app here for better presentation.)</i></p>

<h2>🔐 Data Privacy</h2>
<ul>
  <li>Financial data stays <b>local</b> in <code>finance.json</code>.</li>
  <li>Permissions let users control what data the AI can access.</li>
</ul>

<h2>🤝 Contributing</h2>
<ol>
  <li>Fork the repository</li>
  <li>Create a feature branch (<code>git checkout -b feature-name</code>)</li>
  <li>Commit changes (<code>git commit -m 'Add new feature'</code>)</li>
  <li>Push to branch (<code>git push origin feature-name</code>)</li>
  <li>Open a Pull Request</li>
</ol>

<h2>📜 License</h2>
<p>This project is licensed under the <b>MIT License</b>.</p>

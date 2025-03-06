# **GitHub-Jira Integration Using Flask & Webhooks**

This project integrates **GitHub Issues** with **Jira** using a **Python Flask application** running on **AWS EC2**. When a GitHub issue comment contains `/jira`, a **GitHub webhook** triggers the Flask app, which automatically creates a corresponding Jira issue.

---

## **🚀 Features**
✅ Detects `/jira` in GitHub Issues and creates a Jira ticket.  
✅ Uses **GitHub Webhooks** to trigger the Flask app.  
✅ Runs on **AWS EC2** with a public IP or domain.  
✅ Uses **Jira REST API** to create issues.  

---

## **📌 Architecture**
1. **GitHub Webhook** listens for issue comments.  
2. When a user comments with `/jira`, GitHub sends a **POST request** to the Flask API.  
3. **Flask app parses the request** and creates an issue in Jira. 
---

## **⚙️ Setup Instructions**

### **1️⃣ Deploy Flask App on AWS EC2**
#### **Install Dependencies on EC2**
```bash
sudo apt update && sudo apt install python3-pip -y
pip3 install flask requests
```

#### **Clone the Repository**
```bash
git clone https://github.com/your-repo/github-jira-integration.git
cd github-jira-integration
```

#### **Create `.env` File (Jira API Credentials)**
```bash
echo "JIRA_URL=https://yourcompany.atlassian.net
JIRA_EMAIL=your-email@example.com
JIRA_API_TOKEN=your-api-token
JIRA_PROJECT_KEY=PROJ" > .env
```

#### **Run the Flask App**
```bash
python3 app.py
```
📌 **Your Flask app is now running on `http://EC2-PUBLIC-IP:5000`**

---

### **2️⃣ Configure GitHub Webhook**
1️⃣ Go to your **GitHub repository** → **Settings** → **Webhooks**  
2️⃣ Click **"Add Webhook"**  
3️⃣ Set **Payload URL** to:  
   ```
   http://EC2-PUBLIC-IP:5000/webhook
   ```
4️⃣ Select **Event Trigger: "Issue comments"**  
5️⃣ Click **"Add Webhook"**  

---

## **🔄 Testing the Integration**
1️⃣ **Post a comment on a GitHub issue**:  
```
/jira This needs a Jira ticket.
```
2️⃣ The Flask app will receive the webhook request.  
3️⃣ A Jira issue will be **automatically created**.  
4️⃣ The Jira issue **link will be posted as a GitHub comment**.  
---

## **🎯 Summary**
✅ Flask app runs on **AWS EC2**  
✅ GitHub Webhook triggers **when `/jira` is detected in issues**  
✅ Jira issue is **automatically created** 


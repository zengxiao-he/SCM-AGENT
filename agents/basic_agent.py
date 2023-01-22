"""
Basic SCM Agent - Enhanced with AI capabilities
"""

import os
from openai import OpenAI

class BasicSCMAgent:
    def __init__(self):
        self.name = "SCM-AGENT"
        self.version = "0.2.0"
        self.client = OpenAI(api_key=os.getenv('OPENAI_API_KEY', ''))
    
    def analyze_demand(self, data):
        """Basic demand analysis"""
        if not data:
            return {"error": "No data provided"}
        
        # Simple analysis
        return {
            "status": "analyzed",
            "message": "Basic demand analysis completed",
            "data_points": len(data) if isinstance(data, list) else 1
        }
    
    def get_recommendations(self):
        """Get basic recommendations"""
        return [
            "Monitor inventory levels regularly",
            "Review supplier performance monthly", 
            "Track demand patterns",
            "Implement safety stock policies"
        ]
    
    def get_ai_insights(self, data_summary):
        """Get AI-powered insights"""
        if not self.client.api_key:
            return {"error": "OpenAI API key not configured"}
        
        try:
            prompt = f"Analyze this supply chain data and provide insights: {data_summary}"
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7
            )
            
            return {
                "insights": response.choices[0].message.content,
                "source": "AI Analysis"
            }
        except Exception as e:
            return {"error": f"AI analysis failed: {str(e)}"} 
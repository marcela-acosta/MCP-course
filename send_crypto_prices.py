#!/usr/bin/env python3
"""
Script to send current Bitcoin and Ethereum prices to mpab28@gmail.com
"""

import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

def send_crypto_prices():
    """Send current Bitcoin and Ethereum prices via email"""
    
    # Current prices (from Binance API)
    btc_price = 110056.29
    eth_price = 4271.48
    
    # 24h price changes
    btc_change = -1196.26
    btc_change_percent = -1.075
    eth_change = -35.83
    eth_change_percent = -0.831
    
    # Email configuration
    sender_email = input("Enter your email address: ")
    sender_password = input("Enter your email password (or app password): ")
    recipient_email = "mpab28@gmail.com"
    
    # Create email content
    subject = f"Current Crypto Prices - {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}"
    
    # Determine price change indicators
    btc_indicator = "📈" if btc_change >= 0 else "📉"
    eth_indicator = "📈" if eth_change >= 0 else "📉"
    
    body = f"""Hi,

Here are the current cryptocurrency prices from Binance:

**Bitcoin (BTC)**
💰 Price: ${btc_price:,.2f} USDT
{btc_indicator} 24h Change: {btc_change:+,.2f} USDT ({btc_change_percent:+.3f}%)

**Ethereum (ETH)**
💰 Price: ${eth_price:,.2f} USDT
{eth_indicator} 24h Change: {eth_change:+,.2f} USDT ({eth_change_percent:+.3f}%)

**Market Summary:**
Both Bitcoin and Ethereum are currently in the red for the 24-hour period, with Bitcoin down 1.08% and Ethereum down 0.83%.

Data source: Binance API
Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}

Best regards
"""
    
    # Create message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = subject
    
    # Add body to email
    message.attach(MIMEText(body, "plain"))
    
    # Create SMTP session
    try:
        # For Gmail, use port 587 with TLS
        smtp_server = "smtp.gmail.com"
        port = 587
        
        # Create secure connection
        context = ssl.create_default_context()
        
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls(context=context)
            server.login(sender_email, sender_password)
            
            # Send email
            text = message.as_string()
            server.sendmail(sender_email, recipient_email, text)
            
        print(f"Email sent successfully to {recipient_email}")
        print(f"Bitcoin: ${btc_price:,.2f} ({btc_change_percent:+.3f}%)")
        print(f"Ethereum: ${eth_price:,.2f} ({eth_change_percent:+.3f}%)")
        
    except Exception as e:
        print(f"Error sending email: {e}")
        print("\nTroubleshooting tips:")
        print("1. Make sure you're using an app password for Gmail (not your regular password)")
        print("2. Enable 2-factor authentication on your Gmail account")
        print("3. Generate an app password: https://myaccount.google.com/apppasswords")

if __name__ == "__main__":
    send_crypto_prices()


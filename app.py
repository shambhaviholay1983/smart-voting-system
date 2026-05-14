import os

if __name__ == "__main__":
    # Render कडून मिळणारा पोर्ट वापरा किंवा डिफॉल्ट 5000 वापरा
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
import streamlit as st
import pandas as pd
import numpy as np
import time

# प्रोजेक्ट सेटअप
st.set_page_config(page_title="Future-Genesis: Bio-Digital Twin", layout="wide")
st.title("🧬 Future-Genesis: The World's First Bio-Digital Twin")
st.write("---")

# यूजर इनपुट
user_name = st.text_input("अपना नाम लिखें (Future CEO):", "Ashish")
dna_data = st.text_area("DNA डेटा इनपुट करें (A, T, G, C):", "ATGCGTAC...").upper()

if st.button("🚀 Create My Digital Twin"):
    with st.spinner('ह्यूमन सेल डेटा को डिजिटल कोड में बदला जा रहा है...'):
        time.sleep(3)
        
    st.balloons()
    
    # कैलकुलेशन लॉजिक
    stability = (dna_data.count('G') + dna_data.count('C')) / len(dna_data) * 100
    score = round(stability + 20, 2)

    

site_name = st.text_input("Website Name", "FutureTech")
business = st.text_input("Business Type", "AI Company")
description = st.text_area("About your business", "We build futuristic AI technology.")

if st.button("Generate Website"):

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <title>{site_name}</title>
    <style>
    body {{
        font-family: Arial;
        text-align: center;
        background: #0e1117;
        color: white;
        padding: 50px;
    }}
    h1 {{
        color: #ff4b4b;
    }}
    .box {{
        border: 2px solid #ff4b4b;
        padding: 30px;
        border-radius: 12px;
        max-width: 600px;
        margin: auto;
    }}
    button {{
        background: #ff4b4b;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
    }}
    </style>
    </head>

    <body>

    <div class="box">
    <h1>🚀 {site_name}</h1>
    <h3>{business}</h3>

    <p>{description}</p>

    <button>Contact Us</button>

    </div>

    </body>
    </html>
    """

    st.subheader("Generated Website Code")
    st.code(html, language="html")

    st.download_button(
        label="⬇ Download Website",
        data=html,
        file_name="website.html",
        mime="text/html"
    )import streamlit as st

# 🚀 Aether-Helix Master OS Setup
st.set_page_config(page_title="Aether-Helix: Multi-Tech OS", layout="wide")

# 1. Sidebar - यहाँ से आप टूल चुन सकते हैं
st.sidebar.title("🔗 Universal Control")
app_mode = st.sidebar.selectbox("Choose a Service", ["🧬 Bio-Digital Twin", "🚀 AI Website Builder"])

# --- SECTION 1: BIO-DIGITAL TWIN (पुराना टूल) ---
if app_mode == "🧬 Bio-Digital Twin":
    st.title("🧬 Future-Genesis: Bio-Digital Mirror")
    user_name = st.text_input("अपना नाम लिखें:", "Ashish")
    dna_data = st.text_area("DNA डेटा इनपुट करें (A, T, G, C):", "ATGCGTAC...").upper()
    
    if st.button("🚀 Create Digital Twin"):
        st.balloons()
        if len(dna_data) > 0:
            stability = (dna_data.count('G') + dna_data.count('C')) / len(dna_data) * 100
            st.metric("Genetic Stability", f"{stability:.2f}%")
            st.info(f"नमस्ते {user_name}, आपका डिजिटल जुड़वां तैयार है!")
        else:
            st.warning("कृपया पहले DNA डेटा डालें।")

# --- SECTION 2: AI WEBSITE BUILDER (नया टूल) ---
elif app_mode == "🚀 AI Website Builder":
    st.title("🚀 AI Website Builder")
    st.write("अपना वेबसाइट नाम और बिज़नेस डालें, AI वेबसाइट बना देगा।")

    site_name = st.text_input("Website Name", "FutureTech")
    business = st.text_input("Business Type", "AI Company")
    description = st.text_area("About your business", "We build futuristic AI technology.")

    if st.button("Generate Website"):
        html = f"""
        <html>
        <head>
        <title>{site_name}</title>
        <style>
            body {{ font-family: Arial; text-align: center; background: #0e1117; color: white; padding: 50px; }}
            h1 {{ color: #ff4b4b; }}
            .box {{ border: 2px solid #ff4b4b; padding: 30px; border-radius: 12px; max-width: 600px; margin: auto; }}
        </style>
        </head>
        <body>
            <div class="box">
                <h1>🚀 {site_name}</h1>
                <h3>{business}</h3>
                <p>{description}</p>
            </div>
        </body>
        </html>
        """
        st.subheader("Generated Website Code")
        st.code(html, language="html")
        st.download_button("⬇ Download Website", data=html, file_name="website.html", mime="text/html")

st.sidebar.write("---")
st.sidebar.caption("CEO: Ashish | Future-Genesis Global Operations")
import streamlit as st

# 🚀 Aether-Helix: Universal OS Setup
st.set_page_config(page_title="Aether-Helix: Global OS", layout="wide")

# 1. Sidebar Control
st.sidebar.title("🔗 Universal Control")
app_mode = st.sidebar.selectbox("Choose a Service", ["🧬 Bio-Digital Twin", "🚀 AI Website Builder", "💼 Global Rojgar Engine"])

# --- SECTION 1: BIO-DIGITAL TWIN ---
if app_mode == "🧬 Bio-Digital Twin":
    st.title("🧬 Future-Genesis: Bio-Digital Mirror")
    user_name = st.text_input("अपना नाम लिखें:", "Ashish")
    dna_data = st.text_area("DNA डेटा इनपुट करें (A, T, G, C):").upper()
    if st.button("🚀 Create Digital Twin"):
        st.balloons()
        st.success(f"नमस्ते {user_name}, आपका डिजिटल प्रोफाइल तैयार है!")

# --- SECTION 2: AI WEBSITE BUILDER ---
elif app_mode == "🚀 AI Website Builder":
    st.title("🚀 AI Website Builder")
    site_name = st.text_input("Website Name")
    business = st.text_input("Business Type")
    if st.button("Generate Website"):
        st.code(f"<h1>Welcome to {site_name}</h1><p>AI Generated for {business}</p>", language="html")

# --- SECTION 3: GLOBAL ROJGAR ENGINE (नया टूल) ---
elif app_mode == "💼 Global Rojgar Engine":
    st.title("💼 Universal Rojgar Engine")
    st.write("अपनी स्किल डालें और जानें कि आप **आज से** पैसे कैसे कमा सकते हैं।")
    
    user_skill = st.text_input("आपकी स्किल क्या है? (जैसे: Cooking, Driving, Biology, Coding, Drawing)")
    
    if st.button("Find My Earning Path"):
        st.subheader(f"💡 {user_skill} के जरिए रोजगार के रास्ते:")
        
        if "Biology" in user_skill or "PCB" in user_skill:
            st.info("1. Bio-Data Analyst: लैब डेटा को डिजिटल बनाने में मदद करें।\n2. Online Tutor: छोटे बच्चों को साइंस पढ़ाएं।")
        elif "Coding" in user_skill:
            st.info("1. Freelance Developer: छोटे दुकानदारों के लिए वेबसाइट बनाएं।\n2. Automation Expert: कंपनियों के काम आसान करें।")
        elif "Drawing" in user_skill or "Design" in user_skill:
            st.info("1. NFT Artist: अपनी कला को डिजिटल रूप में बेचें।\n2. Logo Designer: सोशल मीडिया पेज के लिए लोगो बनाएं।")
        else:
            st.info("1. Micro-SaaS: एक छोटी समस्या को कोड से हल करें और बेचें।\n2. Content Creator: अपनी स्किल के बारे में वीडियो बनाकर लोगों को सिखाएं।")
            
        st.success("🔥 टिप: एलन मस्क भी पहले अपनी स्किल (कोडिंग) को फ्रीलांसिंग के जरिए बेचते थे।")

st.sidebar.write("---")
st.sidebar.caption("CEO: Ashish | Future-Genesis Global Operations")
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Aether-Helix Global OS", layout="wide")

# Sidebar
st.sidebar.title("🌍 Aether-Helix Control")
app_mode = st.sidebar.selectbox(
    "Choose Service",
    ["🧬 Bio-Digital Twin", "🚀 AI Website Builder", "💼 Global Rojgar Engine"]
)

# ---------------- BIO DIGITAL TWIN ----------------
if app_mode == "🧬 Bio-Digital Twin":

    st.title("🧬 Bio-Digital Twin Analyzer")

    name = st.text_input("Your Name", "Ashish")
    dna = st.text_area("Enter DNA Sequence (A,T,G,C)", "").upper()

    if st.button("Analyze DNA"):

        if len(dna) == 0:
            st.error("Please enter DNA sequence")
        else:

            counts = {
                "A": dna.count("A"),
                "T": dna.count("T"),
                "G": dna.count("G"),
                "C": dna.count("C")
            }

            df = pd.DataFrame(
                list(counts.items()),
                columns=["Base", "Count"]
            )

            gc = (counts["G"] + counts["C"]) / len(dna) * 100

            st.success(f"Digital Twin created for {name}")

            st.subheader("DNA Composition")
            st.bar_chart(df.set_index("Base"))

            st.metric("GC Stability %", f"{gc:.2f}")

# ---------------- AI WEBSITE BUILDER ----------------
elif app_mode == "🚀 AI Website Builder":

    st.title("🚀 AI Website Builder")

    site = st.text_input("Website Name")
    business = st.text_input("Business Type")
    desc = st.text_area("Business Description")

    if st.button("Generate Website"):

        html = f"""
        <html>
        <head>
        <title>{site}</title>
        <style>
        body {{font-family:Arial;text-align:center;background:#0e1117;color:white;padding:40px}}
        h1 {{color:#ff4b4b}}
        </style>
        </head>

        <body>
        <h1>🚀 {site}</h1>
        <h3>{business}</h3>
        <p>{desc}</p>
        </body>
        </html>
        """

        st.code(html, language="html")

        st.download_button(
            "Download Website",
            html,
            "website.html"
        )

# ---------------- ROJGAR ENGINE ----------------
elif app_mode == "💼 Global Rojgar Engine":

    st.title("💼 Global Rojgar Engine")

    skill = st.text_input("Enter your skill")

    if st.button("Find Opportunities"):

        if "coding" in skill.lower():
            st.success("Freelance Developer, Web App Builder, Automation Expert")

        elif "design" in skill.lower():
            st.success("Logo Designer, UI Designer, NFT Artist")

        elif "biology" in skill.lower():
            st.success("Bio Data Analyst, Research Assistant, Online Tutor")

        else:
            st.info("Content Creator, Micro-SaaS Builder, Online Teacher")

st.sidebar.caption("Future-Genesis Global | CEO: Ashish")
import streamlit as st
import pandas as pd

# 🌍 Global Setup
st.set_page_config(page_title="Aether-Helix Global OS", layout="wide", page_icon="🌍")

# Sidebar - Global Control
st.sidebar.title("🌍 Aether-Helix OS")
menu = st.sidebar.selectbox(
    "Choose Service",
    ["Login", "🧬 Bio-Digital Twin", "🚀 AI Website Builder", "💼 Global Rojgar Engine", "💰 Premium Access"]
)

# ---------------- 1. LOGIN SYSTEM ----------------
if menu == "Login":
    st.subheader("🔐 Future CEO Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "1234":
            st.success(f"Welcome back, CEO {username}!")
            st.balloons()
        else:
            st.error("Invalid credentials. Try again!")

# ---------------- 2. BIO-DIGITAL TWIN (DNA) ----------------
elif menu == "🧬 Bio-Digital Twin":
    st.subheader("🧬 Bio-Digital Twin Analyzer")
    dna = st.text_area("Enter DNA Sequence (A,T,G,C)").upper()

    if st.button("Analyze"):
        if len(dna) > 0:
            counts = {"A": dna.count("A"), "T": dna.count("T"), "G": dna.count("G"), "C": dna.count("C")}
            df = pd.DataFrame(list(counts.items()), columns=["Base","Count"])
            gc = (counts["G"] + counts["C"]) / len(dna) * 100
            
            st.metric("Genetic Stability", f"{gc:.2f}%")
            st.bar_chart(df.set_index("Base"))
            st.info("High Stability detected. Your Digital Twin is ready for space travel! 🚀")
        else:
            st.warning("Please input DNA data first.")

# ---------------- 3. AI WEBSITE BUILDER ----------------
elif menu == "🚀 AI Website Builder":
    st.subheader("🚀 AI Website Generator")
    site = st.text_input("Website Name")
    business = st.text_input("Business Type")

    if st.button("Generate"):
        html = f"<html><body style='text-align:center; background:#111; color:white;'><h1>{site}</h1><p>AI Generated site for {business}</p></body></html>"
        st.code(html, language="html")
        st.download_button("⬇ Download Website File", html, "website.html")

# ---------------- 4. GLOBAL ROJGAR ENGINE ----------------
elif menu == "💼 Global Rojgar Engine":
    st.subheader("💼 Universal Employment & Business Engine")
    skill = st.text_input("अपनी स्किल डालें (e.g. Sales, Coding, Biology)")
    
    if st.button("Find Business Idea"):
        st.success(f"Searching global opportunities for {skill}...")
        if "coding" in skill.lower():
            st.write("💡 Idea: **Micro-SaaS for local shops.** (दुकानदारों के लिए छोटा बिलिंग सॉफ्टवेयर बनाएं)")
        elif "biology" in skill.lower():
            st.write("💡 Idea: **Genomic Data Cleaning.** (लैब के डेटा को साफ़ करने की सर्विस दें)")
        else:
            st.write("💡 Idea: **AI Content Creation.** (कंपनियों के लिए AI से वीडियो बनाएं)")
        st.warning("🔒 Step-by-Step Business Plan के लिए 'Premium Access' लें।")

# ---------------- 5. PREMIUM ACCESS (कमाई का जरिया) ----------------
elif menu == "💰 Premium Access":
    st.subheader("💰 Unlock Aether-Helix Premium")
    st.write("एलन मस्क की तरह अपने बिजनेस को ऑटोमेट (Automate) करें।")
    st.markdown("""
    - ✅ Advanced DNA Mutation Analysis
    - ✅ Professional Business Roadmap
    - ✅ VIP Tech Support
    """)
    st.info("💳 Pay **₹99** to UPI ID: **ashish@upi** (Example)")
    if st.button("Activate Membership"):
        st.warning("Please send payment screenshot to CEO Ashish to activate.")

st.sidebar.write("---")
st.sidebar.caption("Future-Genesis | CEO: Ashish | Version 2.0")
import streamlit as st
import time

# 🌍 Global OS Setup
st.set_page_config(page_title="Aether-Helix: Universal Controller", layout="wide")

# Sidebar - Global Control
st.sidebar.title("🌍 Aether-Helix OS")
menu = st.sidebar.selectbox(
    "Choose Service",
    ["Login", "🤖 Universal Machine Control", "🧬 Bio-Digital Twin", "🚀 AI Website Builder", "💼 Global Rojgar Engine"]
)

# ---------------- 1. UNIVERSAL MACHINE CONTROL (The Hands-Free Engine) ----------------
if menu == "🤖 Universal Machine Control":
    st.header("🤖 Universal Machine Command Center")
    st.write("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("🛰️ Satellites & Drones")
        drone_status = st.toggle("Activate Autonomous Drone Fleet")
        if drone_status:
            st.success("Drones are Airborne. Scanning Global Terrain...")
            st.progress(65) # Battery/Status
        
    with col2:
        st.subheader("🏭 Factory Automation")
        factory_power = st.slider("Production Speed (AI Optimized)", 0, 100, 50)
        st.write(f"Efficiency: {factory_power}%")
        if factory_power > 80:
            st.warning("Warning: Machines Heating Up. Cooling System Active.")

    with col3:
        st.subheader("🏠 Smart Home & IoT")
        lights = st.checkbox("Turn ON Global Operations Lights")
        temp = st.number_input("Global Server Temperature (°C)", 15, 30, 22)

    st.write("---")
    st.subheader("🧠 Neural Command (Hands-Free Mode)")
    command = st.text_input("Enter Voice Command (Simulation):", "Start All Machines")
    
    if st.button("Execute Global Order"):
        with st.spinner("Connecting to Global IoT Grid..."):
            time.sleep(3)
        st.balloons()
        st.success(f"Order Executed: '{command}'. मशीनों ने काम करना शुरू कर दिया है।")
        st.info("💡 Note: असली मशीनें चलाने के लिए आपको उन्हें 'ESP32' या 'Raspberry Pi' जैसे हार्डवेयर से जोड़ना होगा।")

# ---------------- (Baki purane sections yahan add honge) ----------------
elif menu == "Login":
    st.subheader("🔐 Future CEO Login")
    # (Purana login code yahan daal sakte hain)

elif menu == "🧬 Bio-Digital Twin":
    st.subheader("🧬 DNA Analyzer")
    # (Purana DNA code)

st.sidebar.write("---")
st.sidebar.caption("CEO: Ashish | Mission: Full Global Automation")
import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="All Math Engine", layout="wide")

st.title("🧠 Universal Math Solver")

x = sp.symbols('x')

expr_input = st.text_input(
    "Enter mathematical expression (example: x**2 + 3*x + 2)",
    "x**2 + 3*x + 2"
)

if st.button("⚡ Solve All Maths"):

    try:
        expr = sp.sympify(expr_input)

        # Simplify
        simplified = sp.simplify(expr)

        # Solve equation
        solutions = sp.solve(expr, x)

        # Derivative
        derivative = sp.diff(expr, x)

        # Integral
        integral = sp.integrate(expr, x)

        st.subheader("Results")

        st.write("Simplified:", simplified)
        st.write("Solutions:", solutions)
        st.write("Derivative:", derivative)
        st.write("Integral:", integral)

        # Graph plotting
        st.subheader("Graph")

        f = sp.lambdify(x, expr, "numpy")
        xs = np.linspace(-10, 10, 200)
        ys = f(xs)

        fig, ax = plt.subplots()
        ax.plot(xs, ys)
        ax.set_xlabel("x")
        ax.set_ylabel("f(x)")
        ax.set_title("Function Graph")

        st.pyplot(fig)

    except:
        st.error("Invalid mathematical expression")

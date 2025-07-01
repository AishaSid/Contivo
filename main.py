import streamlit as st
import json
from agents import (
    agent_1_topic_analyzer,
    agent_2_script_builder,
    agent_3_seo_optimizer,
    agent_4_script_simplifier,  # <-- Import agent_4
    save_logs_and_output,
    shared_data,
    logs
)

st.set_page_config(page_title="Contivo", layout="centered")

# --- Custom CSS 
st.markdown(
    """
    <style>
    body, .stApp {
        background: linear-gradient(135deg, #070d22 0%, #000000 100%) !important;
        opacity: 0.93;
    }
    .stButton>button {
        background-color: #FFD600 !important;
        color: #222 !important;
        border: none !important;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #FFEA00 !important;
        color: #222 !important;
    }
    </style>
    <div style="height: 100px;"></div>
    <h1 style='text-align: center; font-size: 3.5rem;'>Contivo</h1>
    """, unsafe_allow_html=True)

st.header("Multi-Agent AI Video Content Generator")
st.markdown("This application uses multiple AI agents to generate SEO-optimized content based on your input topic.")

# --- Session State for Topic ---
if "topic" not in st.session_state:
    st.session_state.topic = ""

# --- input Section ---
with st.container():
    col1, col2 = st.columns([4, 1])  # ratio adjustment 
    with col1:
        topic = st.text_input(
            "Enter a topic or keyword",
            placeholder="e.g., Deep Work Techniques",
            key="topic"
        )
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)  # vertical alignment
        generate = st.button("ENTER", key="generate_btn")



# --- output Section ---
if generate:

    if not st.session_state.topic.strip():
        st.warning("Please enter a topic before generating content.")
        st.stop()
    
    # -- for loading, to make it more interactive
    try:
        with st.spinner("Analyzing topic..."):
            try:
                agent_1_topic_analyzer(st.session_state.topic)
                st.success("Topic analyzed successfully.")
            except Exception as e:
                st.error(f"Agent 1 (Topic Analyzer) failed: {e}")

        with st.spinner("Building script..."):
            try:
                agent_2_script_builder()
                st.success("Script built successfully.")
            except Exception as e:
                st.error(f"Agent 2 (Script Builder) failed: {e}")

        with st.spinner("Simplifying script..."):
            try:
                agent_4_script_simplifier()
                st.success("Script simplified for voice-over completed.")
            except Exception as e:
                st.error(f"Agent 4 (Script simplification) failed: {e}")
        
        with st.spinner("Optimizing content for SEO..."):
            try:
                agent_3_seo_optimizer()
                st.success("SEO optimization completed.")
            except Exception as e:
                st.error(f"Agent 3 (SEO Optimizer) failed: {e}")
        
        try:
            save_logs_and_output()
        except Exception as e:
            st.error(f"Saving output failed: {e}")

        # --- Output printing ---
        st.markdown("---")
        st.subheader("Generated Content")
        st.markdown("<h4>Agent-1:</h4>", unsafe_allow_html=True)
        st.markdown(f"**Title:** {shared_data.get('title', 'Not generated')}")
        st.markdown(f"**Description:** {shared_data.get('description', 'Not generated')}")

        st.markdown("<h4>Agent-2:</h4>", unsafe_allow_html=True)
        st.markdown("**Script:**")
        script_content = shared_data.get('script', 'Not generated')
        st.markdown(
            f"<div style='overflow-x: auto; white-space: pre-wrap; word-break: break-word; color: #ffffff;'>{script_content}</div>",
            unsafe_allow_html=True
        )

        st.markdown("<h4>Agent-Bonus:</h4>", unsafe_allow_html=True)
        st.markdown("**Simplified Script for Voice-Over:**")
        simplified_script = shared_data.get("simplified_script", "Not generated").replace("\n", "<br>")
        st.markdown(
            f"<div style='line-height: 1.7; color: #ffffff'>{simplified_script}</div>",
            unsafe_allow_html=True
        )

        st.markdown("<h4>Agent-3:</h4>", unsafe_allow_html=True)
        st.markdown("**Hashtags:**")
        hashtags = shared_data.get("hashtags", [])
        if hashtags:
            colored_hashtags = [f"<span style='color: #1976D2;'>{tag}</span>" for tag in hashtags]
            st.markdown(", ".join(colored_hashtags), unsafe_allow_html=True)
        else:
            st.write("Not generated")

        # --- logs Section ---
        st.markdown("---")
        st.subheader("Agent Logs")
        if logs:
            for log in logs:
                st.info(log)
        else:
            st.write("No logs available.")

        # --- JSON style logs Section ---
        st.markdown("---")
        st.subheader("Agent Logs (JSON)")
        st.code(json.dumps({"logs": logs, "output": shared_data}, indent=4), language="json")

    except Exception as e:
        st.error(f"A critical error occurred: {e}")

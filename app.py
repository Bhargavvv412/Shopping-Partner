import streamlit as st
from agent_config import create_shopping_agent

st.set_page_config(page_title="🛍️ AI Shopping Partner", page_icon="🤖", layout="wide")

st.title("🛍️ AI Shopping Partner (Gemini + Exa)")
st.caption("Find authentic products from trusted e-commerce sites 💡")

query = st.text_area(
    "Describe what you want:",
    placeholder="Example: Black running shoes under ₹10,000 for long-distance running",
    height=100,
)

if st.button("🔍 Search Products"):
    if query.strip():
        with st.spinner("Searching trusted e-commerce sites..."):
            agent = create_shopping_agent()
            response = agent.run(query)

            # ✅ Safely get the actual text
            ai_output = None
            if hasattr(response, "output") and response.output:
                ai_output = response.output
            elif hasattr(response, "messages") and len(response.messages) > 0:
                # Extract last message content
                ai_output = response.messages[-1].content if hasattr(response.messages[-1], "content") else None

            if ai_output:
                st.success("✅ Results ready!")
                st.markdown("### 🧾 Product Recommendations:")
                st.write(ai_output)
            else:
                st.error("⚠️ Agent ran successfully but didn’t return text.")
                st.json(response.model_dump())  # 🔍 Debug full response if needed
    else:
        st.warning("Please enter a product description first.")

st.markdown("---")
st.markdown("👨‍💻 Built by Bhargav | Powered by Gemini + Exa Tools")

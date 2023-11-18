import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Basic Element dalam Streamlit")
st.markdown("""---""")
#--------------------------------------------------------------------------------------------------------
st.header("Write")

st.write(
    """
    # Title Write
    Ini Write()
    """
)
st.write(pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
}))

st.markdown("""---""")
#--------------------------------------------------------------------------------------------------------
st.header("Text")
st.subheader('1. Markdown')
st.markdown(
    """
    # Title Markdown
    Ini markdown()
    """
)

st.subheader('2. Title')
st.title('Ini title()')

st.subheader('3. Header')
st.header('Ini header()')

st.subheader('4. Subheader')
st.subheader('Ini subheader()')

st.subheader('5. Caption')
st.caption('Ini caption()')

st.subheader('6. Code')
code = """def hello():
    print("Hello, ini code()")"""
st.code(code, language='python')

st.subheader('7. Text')
st.text('Halo, ini text(), dibawah ini latex()')

st.subheader('8. Latex')
st.latex(r"""
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
""")

st.markdown("""---""")
#--------------------------------------------------------------------------------------------------------
st.header("Data Display")
st.subheader('1. dataframe()')
df = pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})
st.dataframe(data=df, width=500, height=150)

st.subheader('2. table()')
st.table(data=df)

st.subheader('3. metric()')
st.metric(label="Temperature", value="28 °C", delta="1.2 °C")

st.subheader('4. json()')
st.json({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})

st.markdown("""---""")
#--------------------------------------------------------------------------------------------------------
st.markdown("# Chart")
st.subheader('1. Histogram')
x = np.random.normal(15, 5, 250)
 
fig, ax = plt.subplots()
ax.hist(x=x, bins=15)
st.pyplot(fig)

st.subheader('2. Bar Chart')
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.bar_chart(chart_data)

st.markdown("""---""")
#--------------------------------------------------------------------------------------------------------
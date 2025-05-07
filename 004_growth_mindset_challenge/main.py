#importing the Libraries
import streamlit as st
import pandas as pd 
from io import BytesIO



            
st.set_page_config(page_title="BUTTER CONVERTOR", page_icon="🦋", layout="wide")

st.title(":blue-background[:green[CSV] :orange[⇌] :green[Excel Converter]]")
st.write(":blue-background[:orange[**BUTTER CONVERTOR** 🦋]: Instantly convert your CSV files to Excel and Excel files to CSV — smooth, fast, and hassle-free!]")

  
file_uploader = st.file_uploader("Upload a CSV or Excel file",type=["CSV","xlsx"],accept_multiple_files=True )


if file_uploader:
    for file in file_uploader: 
        if file.name.endswith(".csv"):
            df = pd.read_csv(file)
        elif file.name.endswith(".xlsx"):
            df = pd.read_excel(file)
        else:
            st.error(f"Unsupported file format: {file.name} only xlsx and csv allowed")
            continue


       
        st.write(f"**File name**:{file.name}")
        st.write(f"**File Size**: {file.size} bytes ")
        st.write(f"**Data type**: {file.type}")

         # Display the DataFrame
        st.write("Data Preview:")
        st.dataframe(df.head())

        st.subheader(".🫧Data Cleaning Options")

        if st.checkbox(f"Clean Data for {file.name}"):
            col1,col2 = st.columns(2)

            with col1:
                if st.button("Remove Duplicates"):
                    df.drop_duplicates(inplace=True)
                    st.success("Duplicates removed successfully!")
                    
        
            
            with col2:
                if st.button("Fill Empty Rows"):
                    num_cols = df.select_dtypes(include=['number']).columns
                    df[num_cols] = df[num_cols].fillna(df[num_cols].mean())
                    st.success("Empty rows filled successfully!")


        st.subheader("🔍Select coloumn to convert")
        coloum = st.multiselect(f"Select coloumns to convert {file.name}",df.columns,default=df.columns)


        st.subheader("📺Data visualization ")
        if st.checkbox(f"Show Data Visualization for {file.name}"):
            st.bar_chart(df.select_dtypes(include=['number']).iloc[:,:2])
            


        st.subheader("🔶convertion options")
        conversion_types =st.radio("Select conversion type to:", ["CSV","Excel"], key=file.name)

        if st.button(f"Convert {file.name}"):
            buffer = BytesIO()

            if conversion_types == "CSV":
                df.to_csv(buffer,index=False)
                file_name = file.name.replace(".xlsx", ".csv")
                mine_type = "text/csv"

            if conversion_types == "Excel":
                df.to_excel(buffer, index=False)
                file_name = file.name.replace(".csv", ".xlsx")
                mine_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
           


            st.download_button(label=f"💾Download {file.name} as {conversion_types}", data=buffer, file_name=file_name, mime=mine_type)
        
            st.success(f"{file.name} is converted to {conversion_types}, click on download!")
        st.success("Thank you for using the CSV to Excel Converter!")


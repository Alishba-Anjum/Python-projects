import streamlit as st
import pandas as pd
import os
from io import BytesIO


st.set_page_config(page_title='Data Sweeper', layout='wide')
st.title('💽 Data Sweeper')
st.write('Convert your files format between CSV and xlsx')

uploaded_file = st.file_uploader('Upload your files (CSV or Excel): ', type=['.csv', '.xlsx'])

if uploaded_file:
    file_extension = os.path.splitext(uploaded_file.name)[-1].lower()

    if file_extension == '.csv':
        df = pd.read_csv(uploaded_file)
    elif file_extension == '.xlsx':
        df = pd.read_excel(uploaded_file)
    else:
        st.error(f'Unsupported file type: {file_extension}')

    st.write(f'**File Name:** {uploaded_file.name}')
    st.write(f'**File Size:** {uploaded_file.size/1024}')


    st.write('Preview the head of the Dataframe')
    st.dataframe(df.head())


    st.subheader('📝 Data Cleaning Options')
    if st.checkbox(f'Clean Data for {uploaded_file.name}'):
        col1, col2 = st.columns(2)

        with col1:
            if st.button(f'Remove Duplicates from {uploaded_file.name}'):
                df.drop_duplicates(inplace=True)
                st.write('Duplicates Removed!')

        with col2:
            if st.button(f'Fill missing Values for {uploaded_file.name}'):
                numeric_cols = df.select_dtypes(include=['number']).columns
                df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                st.write('Missing Values have been filled')

        
        st.subheader('Select Columns to Convert')
        columns = st.multiselect(f'Choose columns for {uploaded_file.name}', df.columns, default=df.columns)
        df = df[columns]


        st.subheader('👁‍🗨 Data visualization')
        if st.checkbox(f'Show Visualization for {uploaded_file.name}'):
            st.bar_chart(df.select_dtypes(include='number').iloc[:, :2])


        st.subheader('Conversion Options')
        conversion_type = st.radio(f'Convert {uploaded_file.name} to:', ['CSV', 'Excel'], key=uploaded_file.name)
        if  st.button(f'Convert {uploaded_file.name}'):
            buffer = BytesIO()
            if conversion_type == 'CSV':
                df.to_csv(buffer, index=False)
                file_name = uploaded_file.name.replace(file_extension, '.csv')
                mime_type = 'text/csv'

            elif conversion_type == 'Excel':
                df.to_excel(buffer, index=False)
                file_name = uploaded_file.name.replace(file_extension, '.xlsx')
                mime_type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            buffer.seek(0)


            st.download_button(
                label=f'Download {uploaded_file.name} as {conversion_type}',
                data=buffer,
                file_name=file_name,
                mime=mime_type
            )

st.success('All files uploaded')
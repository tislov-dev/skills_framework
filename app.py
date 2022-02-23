import spacy_streamlit
import streamlit as st
import spacy
import json

nlp = spacy.blank('en')
ruler = nlp.add_pipe("entity_ruler").from_disk('skill_patterns.jsonl')

def main():
    """
    A Simple NLP app for Skills Extraction
    """

    st.title('Skills Extraction Pipeline')

    st.sidebar.header('Description')

    st.sidebar.markdown('''
    This is the pipeline that can extract skills from job reqs, courses and 
    any other text related source. Please enter text in the text area and run.
    ''')


    st.subheader("Named Entity Recognition")
    raw_text = st.text_area("Your Text", placeholder="Enter Text Here")
    st.button('Extract')
    docx = nlp(raw_text)
    spacy_streamlit.visualize_ner(docx,labels=[ent.label_ for ent in docx.ents]) #nlp.get_pipe('entity_ruler').labels


if __name__ == '__main__':
	main()




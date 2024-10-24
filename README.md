# Details of all yamls

  ## Eval:
    
       prerequisite:
         * To do everytime
          - Go to Eval directory
          - Update rag.yaml file with respectiove end points and serving tokens of llm and embedding model
          - Update rag.yaml file with absolute address of the nv_acronym.json file
          - Update eval.yaml file with absolute path of ground truth file and rag.yaml file
          * Need to do sometime:
            - If the ground truth has changed, update the ground truth file with the following three columns:
                 a. Update "answer" column name as "reference_answer"
                 b. Update "question" column name as "normal_question"
                 c. Update "scenario" column name as "question".
            - If any prompt has changed, update the prompt accordingly, following the previous prompt-writing structure:
                 a. In GI, the context is represented as Context:\n {context}\n, using the variable {context}. However, in dkubex_GI_integration, the context variable used is {context_str}.
                 b. In GI, the question is represented as Question: {question}\n, using the variable {question}. However, in dkubex_GI_integration, the question variable used is {query_str}."

      
          command:
                 d3x dataset evaluate --config eval.yaml
          process for eval:
             - Collect the Ground truth file.
             - collect the output of the eval from mlflow.(mlflow->respective experiment->respective run->artifacts->download eval_results_table.json file) <-- final ouput
          run script_for_counting_the_score.py using
             - python3 script_for_counting_the_score.py
             - Note "eval_results_table.json" file should present on the same directory of the script_for_counting_the_score.py file.
             - Update the result here "https://docs.google.com/spreadsheets/d/1BytNWa9fJgxM0-fwrkbZmWnDHcb_Y8iTkuUntLxCBS4/edit?usp=drive_link" 
             - Upload directory on "https://drive.google.com/drive/folders/1y9jy2dpzptjyRtsol6oid19ogTFxIAFe?usp=drive_link" with rag.yaml,eval.yaml,ground_truth,eval_results_table.json files
      
 ## Ingestion:
     using share point and scrapeddata reader:
             d3x dataset ingest -d gi_nv_demo --config /home/data/demo/ingestion_sharepoint_scrapeddata.yaml --client_secret="DCm8Q~glKFasJ9Tt1xtUEi9FD2h77SPhfKnj7aKO" --access_token="access token"
          
      with faq(cache enabled)
                d3x dataset ingest -d gi_nv_demo --config /home/data/demo/ingestion_sharepoint_scrapeddata.yaml --faq --client_secret="DCm8Q~glKFasJ9Tt1xtUEi9FD2h77SPhfKnj7aKO" --access_token="access token"
      Note:
        collect access token from udai and validity of access token is 24hrs.
 ## Cache_disabled:
 prerequisite:
    - Go to Cache_disabled. It contains rag.yaml file without cach enabled.
    - Update rag.yaml file with respective end points and serving tokens of llm and embedding model
    - Update rag.yaml file with absolute address of the nv_acronym.json file
    - Update "securechatapp_using_niceapp.yaml" with "NICE_OPENAI_API_KEY" as securellm application key and update absolute path of rag.yaml and queryrewrite.yaml.
    - Update "securechatapp_without_niceapp.yaml" absolute path of rag.yaml and queryrewrite.yaml
    
    securechat app deploy for nice app:
       d3x apps deploy --config <absolute paths\ of securechatapp_using_niceapp.yaml>
    securechat app deploy not for nice app:
       d3x apps deploy --config <absolute paths\ of securechatapp_without_niceapp.yaml>
    fmquery:
      d3x dataset query -d <dataset name> --config <absolute paths\ of rag.yaml>
 ## Cache_enabled:
 prerequisite:
    - Go to Cache_enabled. It contains rag.yaml file with cach enabled.
    - Update rag.yaml file with respective end points and serving tokens of llm and embedding model
    - Update rag.yaml file with absolute address of the nv_acronym.json file
    - Update "securechatapp_using_niceapp.yaml" with "NICE_OPENAI_API_KEY" as securellm application key and update absolute path of rag.yaml and queryrewrite.yaml.
    - Update "securechatapp_without_niceapp.yaml" absolute path of rag.yaml and queryrewrite.yaml
    
    securechat app deploy for nice app:
       d3x apps deploy --config <absolute paths\ of securechatapp_using_niceapp.yaml>
    securechat app deploy not for nice app:
       d3x apps deploy --config <absolute paths\ of securechatapp_without_niceapp.yaml>
    fmquery:
      d3x dataset query -d <dataset name> --config <absolute paths\ of rag.yaml>

 ## model_configs:
   -contains config.yaml file of lama3.1 with 8k tokens.

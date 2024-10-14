# Details of all yamls

  ## Eval:
    
   prerequisite:
      - Go to Eval directory
      - Update rag.yaml file with respectiove end points and serving tokens of llm and embedding model
      - Update rag.yaml file with absolute address of the nv_acronym.json file
      - Update eval.yaml file with absolute path of ground truth file and rag.yaml file
      
    command:
      - d3x dataset evaluate --config eval.yaml
    process for eval:
      - Collect the Ground truth file.
      - Update the rewrite column as question and question column as original_question and answer as reference_answer.
      - Run eval with only sementic score (hide correctness_evaluator,answer_relevancy_evaluator,retrieval_evaluator scores)
      - collect the output of the eval from mlflow.(mlflow->respective experiment->respective run->artifacts->download eval_results_table.json file)
      - Convert eval_result.json to csv file and gave name as "updated_groundtruth.csv"
      - Run eval with "updated_groundtruth.csv" with parameters correctness_evaluator,answer_relevancy_evaluator,retrieval_evaluator scores except sementic similarity.
      - collect the output of the eval from mlflow.(mlflow->respective experiment->respective run->artifacts->download eval_results_table.json file) <-- final 
         ouput
    run script_for_counting_the_score.py using
      - python3 script_for_counting_the_score.py
      - Note "eval_results_table.json" file should present on the same directory of the script_for_counting_the_score.py file.
      - Update the result here "https://docs.google.com/spreadsheets/d/1BytNWa9fJgxM0-fwrkbZmWnDHcb_Y8iTkuUntLxCBS4/edit?usp=drive_link" 
      - Upload directory on "https://drive.google.com/drive/folders/1y9jy2dpzptjyRtsol6oid19ogTFxIAFe?usp=drive_link" with rag.yaml,          
        eval.yaml,ground_truth,eval_results_table.json files
      
    Prediction:
      - python client/sklearn_titanic_client.py <profile-name> <deployment-name> client/test_file/test.csv
 ## Ingestion:
     - Go to ingestion directory
     using file reader :
      - d3x dataset ingest -d <dataset name> --config <absolute path of the file ingestion.yaml>
    Using scrap_data_reader_ingestion
      - d3x dataset ingest -d <dataset name> --config <absolute path of scrap_data_reader_ingestion.yaml>
          with faq(cache enabled)
      - d3x dataset ingest -d <dataset name> --config <absolute path of scrap_data_reader_ingestion.yaml> --faq
    Using scrapy_reader_ingestion
      - d3x dataset ingest -d <dataset name> --config <absolute path of scrapy_reader_ingestion.yaml>
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

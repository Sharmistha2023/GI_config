# Details of all yamls

  ## Eval:
    command:
      - d3x dataset evaluate --config eval.yaml
    process for eval:
      - Collect the Ground truth file.
      - Update the rewrite column as question and question column as original_question and answer as reference_answer.
      - Run eval with only sementic score (hide correctness_evaluator,answer_relevancy_evaluator,retrieval_evaluator scores)
      - collect the output of the eval from mlflow.(mlflow->respective experiment->respective run->artifacts->download eval_result.json file)
      - Convert eval_result.json to csv file and gave name as "updated_groundtruth.csv"
      - Run eval with "updated_groundtruth.csv" with parameters correctness_evaluator,answer_relevancy_evaluator,retrieval_evaluator scores except sementic similarity.
      - collect the output of the eval from mlflow.(mlflow->respective experiment->respective run->artifacts->download eval_result.json file) <-- final 
         ouput
    run script_for_counting_the_score.py using
      - python3 script_for_counting_the_score.py
      - Note "eval_results_table.json" file should present on the same directory of the script_for_counting_the_score.py file.
      - Update the result here "https://docs.google.com/spreadsheets/d/1BytNWa9fJgxM0-fwrkbZmWnDHcb_Y8iTkuUntLxCBS4/edit?usp=drive_link" 
      - Upload directory on "https://drive.google.com/drive/folders/1y9jy2dpzptjyRtsol6oid19ogTFxIAFe?usp=drive_link" with rag.yaml,          
        eval.yaml,ground_truth,eval_results_table.json files
      
    Prediction:
      - python client/sklearn_titanic_client.py <profile-name> <deployment-name> client/test_file/test.csv
 ## Tensorflow:
    model:
      - d3x mlflow models import tensorflow-model12 tensorflow tensorflow/model/model.keras
    Deploy:
      -  Go to tensorflow folder
      - d3x serve create -n <deployment-name> -r mlflow --model <model-name> --model_version 1 --depfilepath tensorflow_mnist_serve.deploy
    Prediction:
      - python client/tensorflow_client.py <profile-name> <deployment-name> client/images/3.png
                           or
      - python client/tensorflow_mnist_client.py <service-token> <endpoint-url> client/images/3.png
 ## Xgboost:
    model:
      -  d3x mlflow models import xgboost-model xgboost xgboost/model/xgboost_titanic_model.model
    Deploy:
      - Goto xgboost directory
      - d3x serve create -n <deployment-name> -r mlflow --model <model-name> --model_version 1 --depfilepath xgboost_titanic_serve.deploy
    Prediction:
      - python client/xgboost_client.py <profile-name> <deployment-name> client/test_file/test.csv
                                     or
      - python client/xgboost_titanic_client.py <service token> <endpoint> client/test_file/test.csv
  ## Pytorch:
    model:
      -  d3x mlflow models import pytorch-model pytorch pytorch/model/model.pt --class_path pytorch/model/sample.py --class_instance model
    Deploy:
      -  Goto pytorch directory
      - d3x serve create -n <deployment-name> -r mlflow --model <model-name> --model_version 1 --depfilepath pytorch_mnist_serve.deploy
    Prediction:
      - python client/tensorflow_mnist_client.py <profile-name> <deployment-name> client/images/3.png
  ## Custom-model:
    model:
      d3x mlflow models import custom-model custom_model custom_model/model/
    Deploy:
      -Go to custom_model directory
      - d3x serve create -n <deployment-name> -r mlflow --model <model-name> --model_version 1 --depfilepath custom_mnist_serve.deploy
    Prediction:
      - python client/tensorflow_mnist_client.py <profile-name> <deployment-name> client/images/3.png
  

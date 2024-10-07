import json
import os
#from sentence_transformers import CrossEncoder
# import click

class EvalResultsLibrary:
    def __init__(self):
        self.scores_list = []
        self.cross_emb_similarity_scores = []

    def load_eval_results(self):
        # os.chdir('sharmi12')  # Change directory if needed
        file_path = 'eval_results_table.json'
        with open(file_path) as f:
            data = json.load(f)

        columns = data['columns']
        rows = data['data']

        semantic_similarity_idx = columns.index("semantic_similarity_score")
        correctness_idx = columns.index("correctness_score")
        #feedback_idx = columns.index("feedback")
        reference_answer_idx = columns.index("reference_answer")
        outputs_idx = columns.index("ragpipeline_answer")

        self.scores_list = []

        for row in rows:
            scores = {
                "semantic_similarity_score": row[semantic_similarity_idx],
                "correctness_score": row[correctness_idx],
                "reference_answer": row[reference_answer_idx],
                "outputs": row[outputs_idx],
                #"feedback": row[feedback_idx]
            }
            self.scores_list.append(scores)
        
        total_data =    len(self.scores_list)
        semantic_similarity_scores = [entry['semantic_similarity_score'] for entry in self.scores_list]
        correctness_scores = [entry['correctness_score'] for entry in self.scores_list]
        reference_answers = [entry['reference_answer'] for entry in self.scores_list]
        outputs = [entry['outputs'] for entry in self.scores_list]
        #feedback_result = [entry['feedback'] for entry in self.scores_list]

        print(f"Processed {len(self.scores_list)} rows")
        print(f"Semantic Similarity Scores: {len(semantic_similarity_scores)}")
        print(f"Correctness Scores: {len(correctness_scores)}")

        self.reference_answers = reference_answers
        self.outputs = outputs

        #feedback_pos = len([s for s in feedback_result if s != 'na' and s == 'positive'])
        #feedback_neg = len([s for s in feedback_result if s != 'na' and s == 'negative'])
        semantic_similarity_scores_pt_7 = len([s for s in semantic_similarity_scores if s != 'na' and s >= 0.7])
        # semantic_similarity_scores_pt_75 = len([s for s in semantic_similarity_scores if s != 'na' and s >= 0.75])
        semantic_similarity_scores_pt_8 = len([s for s in semantic_similarity_scores if s != 'na' and s >= 0.8])
        semantic_similarity_scores_pt_9 = len([s for s in semantic_similarity_scores if s != 'na' and s >= 0.9])

        #percentage of sementic score
        sementic_percentage_scores_pt_7 =   float((semantic_similarity_scores_pt_7/total_data)*100)
        sementic_percentage_scores_pt_8 =   float((semantic_similarity_scores_pt_8/total_data)*100)
        sementic_percentage_scores_pt_9 =   float((semantic_similarity_scores_pt_9/total_data)*100)

        correctness_scores_pt_7 = len([s for s in correctness_scores if s != 'na' and s >= 7])
        # correctness_scores_pt_6 = len([s for s in correctness_scores if s != 'na' and s < 7])
        correctness_scores_pt_8 = len([s for s in correctness_scores if s != 'na' and s >= 8])
        correctness_scores_pt_9 = len([s for s in correctness_scores if s != 'na' and s >= 9])
        #percentage of correctness score
        correct_percentage_scores_pt_7 =    float((correctness_scores_pt_7/total_data)*100)
        correct_percentage_scores_pt_8 =    float((correctness_scores_pt_8/total_data)*100)
        correct_percentage_scores_pt_9 =    float((correctness_scores_pt_9/total_data)*100)
        


        return {
            # 'semantic_similarity_scores': semantic_similarity_scores,
            # 'correctness_scores': correctness_scores,
            'total_data' :  total_data,
            'semantic_similarity_scores_pt_7': semantic_similarity_scores_pt_7,
            # 'semantic_similarity_scores_pt_75': semantic_similarity_scores_pt_75,
            'semantic_similarity_scores_pt_8': semantic_similarity_scores_pt_8,
            'semantic_similarity_scores_pt_9': semantic_similarity_scores_pt_9,
            'sementic_percentage_scores_pt_7' :  sementic_percentage_scores_pt_7,
            'sementic_percentage_scores_pt_8' :  sementic_percentage_scores_pt_8,
            'sementic_percentage_scores_pt_9' :  sementic_percentage_scores_pt_9,
            'correctness_scores_pt_7': correctness_scores_pt_7,
            # 'correctness_scores_pt_6': correctness_scores_pt_6,
            'correctness_scores_pt_8': correctness_scores_pt_8,
            'correctness_scores_pt_9': correctness_scores_pt_9,
            'correctness_percentage_scores_pt_7' :  correct_percentage_scores_pt_7,
            'correctness_percentage_scores_pt_8' :  correct_percentage_scores_pt_8,
            'correctness_percentage_scores_pt_9' :  correct_percentage_scores_pt_9,
            #'positive feedback': feedback_pos,
            #'negative feedback': feedback_neg,
        }

    def met_scores(self):
        return self.scores_list

    def cross_scores(self):
        model = CrossEncoder(
            model_name="BAAI/bge-reranker-v2-m3", max_length=1024
        )
        self.cross_emb_similarity_scores = []
        for ref_answer, output in zip(self.reference_answers, self.outputs):
            cross_emb_similarity_score = model.predict([ref_answer, output])
            self.cross_emb_similarity_scores.append(float(cross_emb_similarity_score))

        vec_similarity_pt_7 = len([s for s in self.cross_emb_similarity_scores if s != 'na' and s > 0.7])
        vec_similarity_pt_8 = len([s for s in self.cross_emb_similarity_scores if s != 'na' and s > 0.8])
        vec_similarity_pt_9 = len([s for s in self.cross_emb_similarity_scores if s != 'na' and s > 0.9])

        print(f"Total scores processed: {len(self.cross_emb_similarity_scores)}")

        return {
            'cross_emb_similarity_scores': self.cross_emb_similarity_scores,
            'vec_similarity_pt_7': vec_similarity_pt_7,
            'vec_similarity_pt_8': vec_similarity_pt_8,
            'vec_similarity_pt_9': vec_similarity_pt_9,
        }


if __name__ == "__main__":
    eval_library = EvalResultsLibrary()

    # Load evaluation results
    eval_results = eval_library.load_eval_results()

    # Save evaluation results to a file
    with open("output.json", "w") as outfile:
        json.dump(eval_results, outfile, indent=4)
    print("Evaluation Results saved to output.json")

    # Compute cross-scores
    # cross_scores_results = eval_library.cross_scores()

    # Save cross-scores to a file
    # with open("cross_scores_results14.json", "w") as outfile:
    #     json.dump(cross_scores_results, outfile, indent=4)
    # print("Cross Scores saved to cross_scores_results.json")


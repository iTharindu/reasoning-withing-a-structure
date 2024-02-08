# Identifying the limits of transformers when performing model-checking with natural language

#### Authors
1. Tharindu Madusanka
2. Ian Pratt-Hartmann
3. Riza Batista-Navarro

Can transformers learn to comprehend logical semantics in natural language? Although many strands of work on natural language inference have focussed on transformer models’ ability to perform reasoning on text, the above question has not been answered adequately. This is primarily because the logical problems that have been studied in the context of natural language inference have their computational complexity vary with the logical and grammatical constructs within the sentences. As such, it is difficult to access whether the difference in accuracy is due to logical semantics or the difference in computational complexity. A problem that is much suited to address this issue is that of the model-checking problem, whose computational complexity remains constant (for fragments derived from first-order logic). However, the model-checking problem remains untouched in natural language inference research. Thus, we investigated the problem of model-checking with natural language to adequately answer the question of how the logical semantics of natural language affects transformers’ performance. Our results imply that the language fragment has a significant impact on the performance of transformer models. Furthermore, we hypothesise that a transformer model can at least partially understand the logical semantics in natural language but can not completely learn the rules governing the model-checking algorithm.


```
@inproceedings{madusanka-etal-2023-identifying,
    title = "Identifying the limits of transformers when performing model-checking with natural language",
    author = "Madusanka, Tharindu  and
      Batista-navarro, Riza  and
      Pratt-hartmann, Ian",
    editor = "Vlachos, Andreas  and
      Augenstein, Isabelle",
    booktitle = "Proceedings of the 17th Conference of the European Chapter of the Association for Computational Linguistics",
    month = may,
    year = "2023",
    address = "Dubrovnik, Croatia",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2023.eacl-main.257",
    doi = "10.18653/v1/2023.eacl-main.257",
    pages = "3539--3550"
}
```
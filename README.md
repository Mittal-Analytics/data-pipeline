# Data Pipeline
Let's build a data-pipeline to extract structured data from any source.

## What is the required output
To show structured data from any document. The final flow can be something like this:

1. We upload a document: annual report, xbrl, quarterly result file, SAC filing
2. We get a CSV with the data in it.

```text
result date, sales, employee cost, interest cost, manufacturing cost, profit before tax, tax, net profit
2020-03-31,113.22,12.12,14.21,19.89,23.13,7.10,16.03
2019-03-31,103.22,9.17,11.27,16.11,19.13,6.11,13.02
```

We want to create tools that make such conversions possible.

----

## The Pipeline solution
The above problems is a pipeline problem. It involves multiple processes:

1. Getting an input file.
2. Converting that raw data into digital format: eg PDF to text / xml tree.
3. Converting digital format to untagged common format.
4. Creating templates to define tags for specific items in the untagged data.

----

## Milestones

Let's iterate fast. Let's structure the project in 3 parts:

```
extraction/
samples/
frontend/
```

### V0 - Proof of concept

Let's develop a proof of concept.

Write `extract.py` which takes in any file from `samples/annual-reports` and shows `sales` and `profit after tax`.

```bash
python extract.py samples/avantel-2021.pdf
```

Output:

```
item, value, result date, page no
revenue, 776959586, 2021-03-31, 80
revenue, 519193053, 2020-03-31, 80
pat, 153337009, 2021-03-31, 80
pat, 107573913, 2020-03-31, 80
```

### V1 - Have upload and display pipeline

Let's build a basic Flask app (frontend) that makes it easier to try it on multiple files. A GUI will make it easier to test on different files. Let's create a very basic Flask app that allows us to upload file and see results on the web page.

### V2 - Develop more layers

Let's plan more steps once we start reaching here.

![Have a usable product at each stage](https://blog.crisp.se/wp-content/uploads/2016/01/Making-sense-of-MVP-.jpg)



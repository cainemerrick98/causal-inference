# Methods of Causal Inference

In this repo I implement and explain the methods of causal inference by replicating some of the most famous paper in economics and beyond. I can't believe I only stumbled onto causal inference this late in life - thanks Judea Pearl and The Book of Why - and once I started to study it so many past frustrations I experienced on analytics projects made sense. 

Causal inference is the study of the effects of causes, we want to know what will happen to some variable of interest if we intervene on another variable. To me it is science of decision making, it allows us to understand what the effect of an intervention was or predict what will happen if we intervene and therefore allows us to make better decisions. 

Studying causal inference has also allowed me to understand better the limitations of purely predictive models. At one time in my career I was under the impression that prediction was the pinacle of analytics. If we could build a good predictive model for some variable then this was the best we could do. However, as the now well know example from the customer retention space goes, just because we can predict who is going to churn does not mean that we know how to prevent these people from churning. 

For me almost all problems in industry that people try to solve with prediction are actuall more suited to be solved with causal inference. There are a couple of exceptions like fraud detection and default risk on loans where just knowing the probability of a positive case is good enough. However, usually we are trying to improve some metric and have some actions we can take to improve it and this is where we must model the effect of our actions.

## Methods and Papers

Below is a list of the methods I implement and the key paper that I replicated. There is also a short summary of key idea of the method and its usefullness.

1. Matching and Job Training - *LaLonde, R. J. (1986). Evaluating the econometric evaluations of
training programs with experimental data.*

This paper tries studies the causal effect of job training on earnings. It uses data from both a randomised experiment and observational data to see if econometric methods can recover the causal effect 

Matching is a method that takes a control group and tries to make as similar as possible to the treated group to create a credible counterfactual. In this repo I use propensity score matching which matches treated units with control units that had a similar probability of receiving treatment. I also implement a doubly robust estimator which combines an outcome model and a propensity model into one estimator and gives you advantage that if at least one model is correctly specified then your estimate us unbiased.

2. Instrumental Variables and Schooling - *Angrist, Joshua D., and Alan B. Krueger. 1991. "Does Compulsory School Attendance Affect Schooling and Earnings?"*

This paper studies the effect of additional years of schooling on earnings. The authors exploit a natural experiment which meant that children born in Q3 and Q4 of a year would recieve more schooling before they could legally dropout. This natural experiment allows them to set up a instrumental variable research design. 

Instrumental variable designs exploit situations where we have a variable that causes the treatment but does not affect the outcome of interest. The idea is that even if our treatment and outcome are confounded then we can still measure the causal effect of the treatment by only analysing the variation in the treatment caused by the instrumental variable.

3. Difference-In-Differences and Organ Donation - *Kessler, Judd B., and Alvin E. Roth. 2014. "Don't Take 'No' for an Answer: An Experiment with Actual Organ Donor Registrations."*

The authors examine the effect of changing organ donation policy from opt-in to active choice. The dataset contains organ donation rates across US states between 2010-2012. California is the treated unit where active choice was implemented in 2011. To do this they use a DiD research design.

DiD allows us to recover the average treatment effect of the treated by comparing our treated unit(s) with a control under the assumption that the two would have had paralell trends after the treatment date had the treatment not occured. If this assumption holds then difference in the change for the treated unit and the change for control unit is the ATT. In this notebook I only implement the simplest form of DiD (TWFE) but be aware that the research design can become much more complex.

4. Regression Discontinuity and Incumbency Advantage - *Lee, David S. 2008. "Randomized Experiments from Non-random Selection in U.S. House Elections."*

One my favourite research designs as it can produce estimates that are as sound as randomised experiments. In this paper the authors investigate the size of the incumbency advantage for in the US House Of Representatives. Incumbency advantage is the causal effect on the probability of winning an election given you won the last one (are the incumbent).

RDDs exploit the fact that we know exactly how treatment is assigned. It requires that there is some continuous variable and at some value treatment is guaranteed or the probability of treatment is much higher. We compare units just under and just over this threshold, assuming that assignment to treatment between these two groups is essentially random, to get the ATE.

5. Synthetic Control and Smoking Reduction - *Abadie, A., Diamond, A., & Hainmueller, J. (2007). *Synthetic control methods for comparative case studies: Estimating the effect of California's Tobacco Control Program*

The authors investigate the impact of California's proposition 99, a piece of anti-smoking legislation, on the consumption of cigarettes. They use data on cigarette sales aggregated at the state and year level.

Synthetic control is all about building a good control when you don't have one. You have a set of units, one of which is treated and the others are known as the donor pool. You want to find some linear combination of the donor pool which minimises the pre-intervention (before the treatment) distance in the outcome variable between the treated unit and the linear combination of the donor pool.

## Running the code

* clone this repo locally
* set up a venv
* pip install requirements.txt
* good to go!


## Resources

Here are some of the best resources for understanding the methods of causal inference

* The Book of Why - Judea Pearl
* Causal Inference The Mixtape - Scott Cunningham
* The Effect - Nick Huntington Klein
* Causal Inference for the Brave and True - Matheus Facure
* Causal Inference In Statistics A Primer - Judea Pearl
# Traffic Flow Prediction with Linear method


## Requirement
- numpy    

## Description
Take the prediction of flow profile at a given location as an example. We assume that the dynamic statistical flow profiles are normally distributed. The flow profile vector conditioned on the current measurement can be forecasted by the following best linear predictor:

**Core function:**

![function](/linear_method/formula1.png)


where *q_f =col(q(k+1),···,q(k+n))* denotes the extended flow vector to be forecasted for the coming predicting horizon, *q_f* is the corresponding historical data during the same period with *E(q_f)* denotes the mean value of *q_f*, while *q_m = col(q((k−l+1)),··· , q(k))* is the measured flow vector for current time period. *S_(qˆ (f,m))* denotes the covariance matrix between *q_f* and *q_m*.

![mechanism](/linear_method/description.png)


The mechanism of the best linear predictor is depicted above. We utilize the difference between the historical mean and current measurement of the flow profile (we will refer to this as “error”) to correct the prediction. Ideally, if this error is zero, the predicted flow profile “equals to” the historical flow profile, or no adjustment is made. Otherwise, we adjust the prediction by the error weighted by the covariance matrices (or their inverses) if the error is not zero. The best linear predictor can forecast the flow profiles and supply functions by considering their historical statistics and the real-time detection. This method avoids the time consuming approaches such as data mining in database (e.g. k-NN algorithm). Thus, it is efficient. Adopting the time-dependent supply functions instead of the fixed parameters renders the prediction of traffic state more reliable.


The linear predictor adopted here is based on the experience of *PATH*, see *Reference*. The reason is that occupancies and volumes obtained from detectors at nearby locations are highly correlated. Therefore, measurements from one location can be used to estimate quantities at other locations, and a more accurate estimate can be formed if all the neighboring detectors are used in the estimation. As deemed by Chen et al. Chen et al. (2003) that **“The high correlation among neighboring measurements means that linear regression is a good way to predict one from the other. It is also easy to implement and fast to run.”**

## Experiment


These are the result for the traffic flow prediction experiment.
![evaluate](/linea_method.png)

## Reference

	@article{  
	  title={Detecting errors and imputing missing data for single loop surveillance systems},  
	  author={C Chen, J Kwon, J Rice, A Skabardonis, P Varaiya},
	  journal={Transportation Research Record No. 1855, 160-167},
	  year={2003}
	}
	



# Traffic Flow Prediction with Linear method


## Requirement
- numpy    

## Description
Here are some maths description of this method
**Core function:**
```
write it latter
```
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
	



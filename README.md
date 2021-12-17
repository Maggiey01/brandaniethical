# brandaniethical

A package for green consumers and investors to quickly get a view of fashion brands’ animal policy, rate, and animal material usage. and check trendy tickers esg from yahoo finance and esg api

### Function1 - brandaniethical(brandlist)
    
    """
    Get fashion brands' animal ethical usage information. provide information of whether the brand use fur, angora, down feather, shearling, karakul, exotic animal skin and hair, wool use including ‘mulesing’, and leather 
    Also check whether brands use these material align with standards.
    
    Parameters
    ----------
    brandlist : list
      A list of brands name that consumers want to know their condition of animal usage
    
    Returns
    -------
    pandas.dataframe
      The dataframe of brands ethical consumption of animal material which include usage of fur, angora, down feather, shearling, karakul, exotic animal skin and hair, wool use including ‘mulesing’, and leather. Also check whether brands use these material align with standards.
      
    Examples
    --------
    >>> from brandaniethical import brandaniethical 
    >>> brandaniethical.brandaniethical(['cos','theory','lululemon','nike', 'skechers'])
	company	animal_score	update	fur	angora	leather	wool	shearling	karakul	down	feather	exotic animal hair	exotic animal skin	down_RDS	wool_mulesing
0	cos	3/5	July 2020	0	0	1	1	0	0	1	0	1	0	1	1
1	theory	2/5	December 2019	0	0	1	1	0	0	1	0	1	0	0	0
2	lululemon	2/5	July 2020	0	0	1	1	0	0	1	0	1	0	1	0
3	nike	2/5	July 2020	0	0	1	1	0	0	1	0	1	0	0	0
4	skechers	2/5	August 2020	0	0	1	1	0	0	0	0	0	0	0	0
    
    """
    
### Function2: trendyesg(region, start=5)
    """
    Get region's trendy tickers' esg score based on given region and regular rank of market price.

    Parameters
    ----------
    region : string
      A string that limit the region of market consumers are interested in, which include US, BR, AU, CA, FR, DE, HK, IN, IT, ES, GB, and SG.
    start : int
      A int that indicate the ranking .

    Returns
    -------
    pandas.dataframe
      The dataframe of trendy tickers' esg, environmental, social,governance score, and its ticker based on consumers interested region and the lowest ranking consumers want to start to look at

    Examples
    --------
    >>> from brandaniethical import trendyesg 
    >>> trendyesg(region='US',start =8)
	company_name	env_score	soc_score	gov_score	total	ticker
0	Medtronic plc	500	304	310	1114	MDT
1	Pfizer Inc.	510	300	305	1115	PFE
2	Roblox Corporation	245	304	220	769	RBLX
3	Lemonade, Inc.	520	303	300	1123	LMND
4	Nucor Corporation	251	326	210	787	NUE
    
    """
    

## Installation

```bash
$ pip install brandaniethical
```

## Usage

- TODO

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`brandaniethical` was created by Yang Hu. It is licensed under the terms of the MIT license.

## Credits

`brandaniethical` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).

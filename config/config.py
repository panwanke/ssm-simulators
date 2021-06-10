from basic_simulators import boundary_functions as bf

model_config = {'ddm': {'name': 'ddm',
                        'params':['v', 'a', 'z', 't'],
                        'param_bounds': [[-3.0, 0.3, 0.1, 0.0], [3.0, 2.5, 0.9, 2.0]],
                        'boundary': bf.constant,
                        'n_params': 4,
                        'default_params': [0.0, 1.0, 0.5, 1e-3],
                        'hddm_include': ['z']},
                'angle':{'name': 'angle',
                        'params': ['v', 'a', 'z', 't', 'theta'],
                         'param_bounds': [[-3.0, 0.3, 0.2, 1e-3, -0.1], [3.0, 2.0, 0.8, 2.0, 1.45]],
                        'boundary': bf.angle,
                        'n_params': 5,
                        'default_params': [0.0, 1.0, 0.5, 1e-3, 0.0],
                        'hddm_include':['z', 'theta']},
                'weibull':{'name': 'weibull',
                           'params': ['v', 'a', 'z', 't', 'alpha', 'beta'],
                           'param_bounds': [[-2.5, 0.3, 0.2, 1e-3, 0.31, 0.31], [2.5, 2.5, 0.8, 2.0, 4.99, 6.99]],
                          'boundary': bf.weibull_cdf,
                          'n_params': 6,
                          'default_params': [0.0, 1.0, 0.5, 1e-3, 3.0, 3.0],
                          'hddm_include': ['z', 'alpha', 'beta']},
                'levy':{'name': 'levy',
                        'params':['v', 'a', 'z', 'alpha', 't'],
                        'param_bounds':[[-3.0, 0.3, 0.1, 1.0, 1e-3], [3.0, 2.0, 0.9, 2.0, 2]],
                        'boundary': bf.constant,
                        'n_params': 5,
                         'default_params': [0.0, 1.0, 0.5, 1.5, 1e-3],
                         'hddm_include': ['z', 'alpha']},
                'full_ddm':{'name': 'full_ddm',
                            'params':['v', 'a', 'z', 't', 'sz', 'sv', 'st'],
                            'param_bounds':[[-3.0, 0.3, 0.3, 0.25, 1e-3, 1e-3, 1e-3], [3.0, 2.5, 0.7, 2.25, 0.2, 2.0, 0.25]],
                            'boundary': bf.constant,
                            'n_params': 7,
                            'default_params': [0.0, 1.0, 0.5, 0.25, 1e-3, 1e-3, 1e-3],
                            'hddm_include': ['z', 'st', 'sv', 'sz']},
                'ornstein':{'name': 'ornstein', 
                            'params':['v', 'a', 'z', 'g', 't'],
                            'param_bounds':[[-2.0, 0.3, 0.2, -1.0, 1e-3], [2.0, 2.0, 0.8, 1.0, 2]],
                            'boundary': bf.constant,
                            'n_params': 5,
                            'default_params': [0.0, 1.0, 0.5, 0.0, 1e-3],
                            'hddm_include': ['z', 'g']},
                'ddm_sdv':{'name': 'ddm_sdv',
                           'params':['v', 'a', 'z', 't', 'sv'],
                           'param_bounds':[[-3.0, 0.3, 0.1, 1e-3, 1e-3],[ 3.0, 2.5, 0.9, 2.0, 2.5]],
                           'boundary': bf.constant,
                           'n_params': 5,
                           'default_params': [0.0, 1.0, 0.5, 1e-3, 1e-3],
                           'hddm_include': ['z', 'sv']
                           },
                'glob':{'name': 'glob',
                        'params': ['v', 'a', 'z', 'alphar', 'g', 't', 'theta'],
                       'param_bounds': [[-3.0, 0.3, 0.15, 1.0, -1.0, 1e-5, -0.1], [3.0, 2.0, 0.85, 2.0, 1.0, 2.0, 1.45]],
                       'n_params': 7,
                       'default_params': [0.0, 1.0, 0.5, 2.0, 0.0, 1.0, 0.0],
                       'hddm_include': ['z', 'alphar', 'g', 'theta']
                       },
                }

model_config['weibull_cdf'] = model_config['weibull'].copy()
model_config['full_ddm2'] = model_config['full_ddm'].copy()


#### DATASET GENERATOR CONFIGS ----------------------------------------------------------------

kde_simulation_filters = {'mode': 20, # != (if mode is max_rt)
                          'choice_cnt': 10, # > (each choice receive at least 10 samples in simulator)
                          'mean_rt': 15, # < (mean_rt is smaller than specified value
                          'std': 0, # > (std is positive for each choice)
                          'mode_cnt_rel': 0.5  # < (mode does not receive more than a proportion of samples for each choice)
                         }


data_generator_config = {'lan': {'mlp': {'output_folder': 'data/lan_mlp/',
                                        'dgp_list': ['ddm'],
                                        'nbins': 0,
                                        'n_samples': {'low': 100000, 'high': 100000},
                                        'n_parameter_sets': 10000,
                                        'n_parameter_sets_rejected': 100,
                                        'n_training_samples_by_parameter_set': 1000,
                                        'max_t': 20,
                                        'delta_t': 0.001,
                                        'pickleprotocol': 4,
                                        'n_cpus': 'all',
                                        'kde_data_mixture_probabilities': [0.8, 0.1, 0.1],
                                        'simulation_filters': kde_simulation_filters,
                                        'negative_rt_ll': -66.77497,
                                        'n_subruns': 10},
                                 'cnn': {'output_folder': 'data/lan_cnn/',
                                        'dgp_list': ['ddm'],
                                        'nbins': 512,
                                        'n_samples': 100000,
                                        'max_t': 20.0,
                                        'delta_t': 0.001},
                                 }
}







##### -------------------------------------------------------------------------------------------
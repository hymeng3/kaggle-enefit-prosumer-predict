import enefit
​
env = enefit.make_env()
iter_test = env.iter_test()
​
for (
        test,
        revealed_targets,
        client,
        historical_weather,
        forecast_weather,
        electricity_prices,
        gas_prices,
        sample_prediction
) in iter_test:
​
    if test.iloc[0]['currently_scored'] == False:
        print(f'currently_scored is false, just creating a dummy prediction')
        sample_prediction["target"] = 0.0
​
        env.predict(sample_prediction)
        continue
    print('currently_scored is true, predicting 1000.0 always')
    sample_prediction["target"] = 1000.0
    env.predict(sample_prediction)

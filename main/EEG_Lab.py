def Power(subject_data, save=False):

  #subject_data = subj_1['train_data_class1']
  data = subject_data
  FFT = []
  t = np.linspace(0,3,7200)
  f = np.linspace(1/3, 2400, 7200)
  f_cut_min = 10
  f_cut_max = 150
  for trial in data:
    fft = np.fft.fft(trial.T)
    fft = fft.T
    fft = fft[(f>f_cut_min)*(f<f_cut_max),:]

    FFT.append(fft)
  FFT = np.array(FFT)
  f = f[(f>f_cut_min)*(f<f_cut_max)]
  power = np.sum(np.abs(FFT), axis=1)
  return power

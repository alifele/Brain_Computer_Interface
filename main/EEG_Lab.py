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




def STFT_calculator(all_data, window_size=1500, fs=1500, total_t=6, f_cut=30, show=False, filter=False, channel=0):

  FFT = []
  f = np.linspace(1/total_t, fs, window_size)
  t = np.linspace(0, total_t,int(total_t*fs))

  for shift in range(1, t.shape[0] - window_size):
    data = all_data[shift:shift+window_size, :]
    fft = np.fft.fft(data.T)
    fft = fft.T
    fft = fft [f<f_cut,:]
    FFT.append(fft.tolist())

  FFT = np.array(FFT)
  print(FFT.shape)

  STFT = np.abs(FFT[:,::-1, :])

  if filter == True:
    mean = 500
    STFT_ = STFT.copy()
    for i in range(mean,np.shape(STFT)[1]-mean):
      STFT_[:,i] = np.min([STFT[:,i-j] for j in range(-mean,mean+1)], axis=0)
     
    STFT = STFT_

  if show == True:
    plt.imshow(STFT[:,:,channel].T, extent=[0, total_t, 1/total_t, f_cut], aspect='auto')


  return STFT





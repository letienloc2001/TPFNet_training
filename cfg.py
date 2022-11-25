class Config:
    # paths for synthetic train dataset
    train_x = '/content/drive/Shareddrives/HCMUT/DACN/data_collection/SCUT-EnsText/syn_train/img/*.png'
    train_y = '/content/drive/Shareddrives/HCMUT/DACN/data_collection/SCUT-EnsText/syn_train/label/*.png'
    train_mask = '/content/drive/Shareddrives/HCMUT/DACN/data_collection/SCUT-EnsText/train/all_gts/*.txt'
    # paths for synthetic test Dataset
    test_x = '/content/drive/Shareddrives/HCMUT/DACN/data_collection/SCUT-EnsText/syn_test/img/*.png'
    test_y = '/content/drive/Shareddrives/HCMUT/DACN/data_collection/SCUT-EnsText/syn_test/label/*.png'
    test_mask = '/content/drive/Shareddrives/HCMUT/DACN/data_collection/SCUT-EnsText/test/all_gts/*.txt'

    # # paths for SCUT-real train Dataset
    # train_x = 'Data/real/train/all_images/*.jpg'
    # train_y = 'Data/real/train/all_labels/*.jpg'
    # train_mask = 'Data/real/train/all_gts/*.txt'

    # # paths for SCUT-real test Dataset
    # test_x = 'Data/real/test/all_images/*.jpg'
    # test_y = 'Data/real/test/all_labels/*.jpg'
    # test_mask = 'Data/real/test/all_gts/*.txt'


    # train conig
    batch_size = 32
    epochs=400
    saved_model_path = 'saved_model/'
    num_worker=3
    lr=1e-4

    

class Config:
    # paths for synthetic train dataset
    train_x = '/content/drive/Shareddrives/HCMUT/Thesis/data/places265/village/input/train/*.jpg'
    train_y = '/content/drive/Shareddrives/HCMUT/Thesis/data/places265/village/target/train/*.jpg'
    # train_mask = '/content/drive/Shareddrives/HCMUT/DACN/data_collection/SCUT-8K/syn_train/bbox/*.txt'
    # paths for synthetic test Dataset
    test_x = '/content/drive/Shareddrives/HCMUT/Thesis/data/places265/village/input/val/*.jpg'
    test_y = '/content/drive/Shareddrives/HCMUT/Thesis/data/places265/village/target/val/*.jpg'
    # test_mask = '/content/drive/Shareddrives/HCMUT/DACN/data_collection/SCUT-8K/syn_test/bbox/*.txt'

    # # paths for SCUT-real train Dataset
    # train_x = 'Data/real/train/all_images/*.jpg'
    # train_y = 'Data/real/train/all_labels/*.jpg'
    # train_mask = 'Data/real/train/all_gts/*.txt'

    # # paths for SCUT-real test Dataset
    # test_x = 'Data/real/test/all_images/*.jpg'
    # test_y = 'Data/real/test/all_labels/*.jpg'
    # test_mask = 'Data/real/test/all_gts/*.txt'


    # train conig
    batch_size = 8
    epochs=400
    saved_model_path = '/content/drive/Shareddrives/HCMUT/Thesis/checkpoint/TPFNet/'
    num_worker=4
    lr=1e-4

    

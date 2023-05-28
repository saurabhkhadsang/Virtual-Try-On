import subprocess
from django.shortcuts import render,redirect
from django.http import HttpResponse
import os



def upload_images(request):
    if request.method == 'POST':
        image1 = request.FILES.get('image1')
        image2 = request.FILES.get('image2')
        
        # Specify the directory to save the images
        save_directory = 'D:\MP3_Django_Test_2_W\myproject\_INPUT'
        save_directory_cloth = 'D:\MP3_Django_Test_2_W\myproject\_INPUT\cloth'
        save_directory_pose = 'D:\MP3_Django_Test_2_W\myproject\_INPUT\pose'
        
        # Create the save directory if it doesn't exist
        # if not os.path.exists(save_directory):
        #     os.makedirs(save_directory)
        
        # Save the uploaded images to the specified directory
        with open(os.path.join(save_directory_pose, image1.name), 'wb') as f:
            for chunk in image1.chunks():
                f.write(chunk)
        
        with open(os.path.join(save_directory_cloth, image2.name), 'wb') as f:
            for chunk in image2.chunks():
                f.write(chunk)
        
        # return HttpResponse("Images uploaded successfully!")
        return render(request,'template.html')
    
    # return render(request, 'upload_images.html')


def run_scripts(request):

    # Resize and Rename Cloth|Pose
    resize_rename_cloth_pose = r'cmd.exe /C D: && cd D:\MP3_Django_Test_2_W\myproject\XY_Copy && python resize_rename.py'
    subprocess.call(resize_rename_cloth_pose, shell=True)


    # Human Parse
    Input_Human_Parse_W = r'cmd.exe /C D: && cd D:\MP3_Django_Test_2_W\myproject\XY_Copy && python Input_Human_Parse_FROM_Pose.py'
    command_Human_Parse_W = r'cmd.exe /C D: && cd D:\MP3_Django_Test_2_W\myproject\Human_Parse_W\image_segmentation\human_part_segmentation && call venv\Scripts\activate.bat && python human_part_segmentation_atr.py && python human_part_segmentation_lip.py && python palette.py && python clean_mask.py'
    Output_Human_Parse_W = r'cmd.exe /C D: && cd D:\MP3_Django_Test_2_W\myproject\XY_Copy && python Output_Human_Parse_TO_image_parse_v3.py'
    subprocess.call(Input_Human_Parse_W, shell=True)
    subprocess.call(command_Human_Parse_W, shell=True)
    subprocess.call(Output_Human_Parse_W, shell=True)


    # Dense Pose
    Input_DenseP_W = r'cmd.exe /C D: && cd D:\MP3_Django_Test_2_W\myproject\XY_Copy && python Input_DenseP_FROM_Pose.py'
    command_DenseP_W = r'cmd.exe /C D: && cd D:\MP3_Django_Test_2_W\myproject\DenseP_W && call venv\Scripts\activate.bat && cd .\detectron2\projects\DensePose\ && python apply_net.py show configs/densepose_rcnn_R_50_FPN_s1x.yaml https://dl.fbaipublicfiles.com/densepose/densepose_rcnn_R_50_FPN_s1x/165712039/model_final_162be9.pkl image_path dp_segm -v --opts MODEL.DEVICE cpu'
    Output_DenseP_W = r'cmd.exe /C D: && cd D:\MP3_Django_Test_2_W\myproject\XY_Copy && python Output_DenseP_TO_image_densepose.py'
    subprocess.call(Input_DenseP_W, shell=True)
    subprocess.call(command_DenseP_W, shell=True)
    subprocess.call(Output_DenseP_W, shell=True)


    # Open Pose
    Input_OpenP_W = r'cmd.exe /C D: && cd D:\MP3_Django_Test_2_W\myproject\XY_Copy && python Input_OpenP_FROM_Pose.py'
    command_OpenP_W = r'cmd.exe /C D: && cd D:\MP3_Django_Test_2_W\myproject\OpenP_W\openpose && call bin\OpenPoseDemo.exe --image_dir examples\media --hand --write_images output\ --write_json output/ --disable_blending'
    Output_OpenP_W = r'cmd.exe /C D: && cd D:\MP3_Django_Test_2_W\myproject\XY_Copy && python Output_Openpose_TO_openpose.py'
    subprocess.call(Input_OpenP_W, shell=True)
    subprocess.call(command_OpenP_W, shell=True)
    subprocess.call(Output_OpenP_W, shell=True)


    # Cloth Mask
    Input_X_Cloth_Mask_W = r'cmd.exe /C D: && cd D:\MP3_Django_Test_2_W\myproject\XY_Copy && python Input_X_Cloth_Mask_FROM_cloth.py'
    command_X_Cloth_Mask_W = r'cmd.exe /C D: && cd D:\MP3_Django_Test_2_W\myproject\X_Cloth _Mask_W && call venv\Scripts\activate.bat && python .\cloth-seg\infer.py && python color.py --type 1 && cd ./cloth-seg && python clean_mask.py'
    Output_X_Cloth_Mask_W = r'cmd.exe /C D: && cd D:\MP3_Django_Test_2_W\myproject\XY_Copy && python Output_X_Cloth_mask_TO_cloth_mask.py'
    subprocess.call(Input_X_Cloth_Mask_W, shell=True)
    subprocess.call(command_X_Cloth_Mask_W, shell=True)
    subprocess.call(Output_X_Cloth_Mask_W, shell=True)


    # Human and Parse Agnostic
    Input_Human_Parse_Agnostic = r'cmd.exe /C D: && cd D:\MP3_Django_Test_2_W\myproject\XY_Copy && python Input_Parse_and_Human_Agnostic_FROM_res_Three.py'
    command_Human_Parse_Agnostic = r'cmd.exe /C D: && cd D:\MP3_Django_Test_2_W\myproject\X_Parse_Agnostic_W && call venv\Scripts\activate.bat && python main_Parse_Agnostic.py && python main_Human_Agnostic.py'
    Output_Human_Parse_Agnostic = r'cmd.exe /C D: && cd D:\MP3_Django_Test_2_W\myproject\XY_Copy && python Output_X_Parse_and_Human_Agnostic_TO_resp_agnostic.py'
    subprocess.call(Input_Human_Parse_Agnostic, shell=True)
    subprocess.call(command_Human_Parse_Agnostic, shell=True)
    subprocess.call(Output_Human_Parse_Agnostic, shell=True)


    # Data -> HR-VITON/DATA
    copy_Data_TO_HRVITON = r'cmd.exe /C D: && cd D:\MP3_Django_Test_2_W\myproject\XY_Copy && python copy_Data_TO_HRVITON.py'
    subprocess.call(copy_Data_TO_HRVITON, shell=True)


    # RUN HR-VITON
    run_VITON = r'cmd.exe /C D: && cd D:\MP3_Django_Test_2_W\myproject\_HR_VITON_W\HR-VITON && call venv\Scripts\activate.bat && python test_generator.py --occlusion --test_name test_name1 --tocg_checkpoint "mtviton.pth" --gen_checkpoint "gen.pth" --datasetting unpaired --dataroot "data" --data_list "test_pairs.txt"'
    subprocess.call(run_VITON, shell=True)


    # Copy Output to HRVITON/OUTPUT
    copy_HRVITON_output_to_output = r'cmd.exe /C D: && cd D:\MP3_Django_Test_2_W\myproject\XY_Copy && python copy_HRVITON_Output_TO_Output.py'
    subprocess.call(copy_HRVITON_output_to_output, shell=True)

    # Copy Output to Django/Static
    copy_Output_TO_Django_Image = r'cmd.exe /C D: && cd D:\MP3_Django_Test_2_W\myproject\XY_Copy && python copy_Output_TO_Django_Image.py'
    subprocess.call(copy_Output_TO_Django_Image, shell=True)
    
    

    # return HttpResponse("Scripts executed successfully!")
    return render(request,'output.html')


def index(request):
    return render(request, 'upload_images.html')




# ===========================================================================================================================================/
# ===========================================================================================================================================/
# ===========================================================================================================================================/
# ===========================================================================================================================================/
# ===========================================================================================================================================/
# ===========================================================================================================================================/






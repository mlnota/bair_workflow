from bair_analysis.utils import ANALYSIS_DIR, SUBJECTS_DIR
from bair_analysis.workflows.spatialobject import (
    create_workflow_spatialobject_7T,
    )


def test_workflow_spatialobject_7T():
    w = create_workflow_spatialobject_7T()

    input_node = w.get_node('input')
    input_node.inputs.t1w = str(
        SUBJECTS_DIR
        / 'sub-beilen/ses-UMCU7Tdaym13/anat/sub-beilen_ses-UMCU7Tdaym13_acq-wholebrain_T1w.nii')
    input_node.inputs.t2star_fov = str(
        SUBJECTS_DIR
        / 'sub-beilen/ses-UMCU7Tdaym13/T2star/sub-beilen_ses-UMCU7Tdaym13_acq-visualcortex_T2star.nii.gz')
    input_node.inputs.t2star_whole = str(
        SUBJECTS_DIR
        / 'sub-beilen/ses-UMCU7Tdaym13/T2star/sub-beilen_ses-UMCU7Tdaym13_acq-wholebrain_T2star.nii.gz')
    input_node.inputs.bold = str(
        SUBJECTS_DIR
        / 'sub-beilen/ses-UMCU7Tdaym13/func/sub-beilen_ses-UMCU7Tdaym13_task-bairspatialobject_run-1_bold.nii')
    input_node.inputs.events = str(
        SUBJECTS_DIR
        / 'sub-beilen/ses-UMCU7Tdaym13/func/sub-beilen_ses-UMCU7Tdaym13_task-bairspatialobject_run-1_events.tsv')

    w.base_dir = str(ANALYSIS_DIR)
    w.write_graph(graph2use='flat')
    w.write_graph(graph2use='colored')

    w.run(plugin='MultiProc')

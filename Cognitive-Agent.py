# Your Agent for solving Raven's Progressive Matrices. You MUST modify this file.
#
# You may also create and submit new files in addition to modifying this file.
#
# Make sure your file retains methods with the signatures:
# def __init__(self)
# def Solve(self,problem)
#
# These methods will be necessary for the project's main method to run.

# Install Pillow and uncomment this line to access image processing.
from itertools import izip
from PIL import Image, ImageChops, ImageFilter
import PIL

class Agent:
    # The default constructor for your Agent. Make sure to execute any
    # processing necessary before your Agent starts solving problems here.
    #
    # Do not add any variables to this signature; they will not be used by
    # main().
    def __init__(self):
        pass

    # The primary method for solving incoming Raven's Progressive Matrices.
    # For each problem, your Agent's Solve() method will be called. At the
    # conclusion of Solve(), your Agent should return an integer representing its
    # answer to the question: "1", "2", "3", "4", "5", or "6". These integers
    # are also the Names of the individual RavensFigures, obtained through
    # RavensFigure.getName() (as Strings).
    #
    # In addition to returning your answer at the end of the method, your Agent
    # may also call problem.checkAnswer(int givenAnswer). The parameter
    # passed to checkAnswer should be your Agent's current guess for the
    # problem; checkAnswer will return the correct answer to the problem. This
    # allows your Agent to check its answer. Note, however, that after your
    # agent has called checkAnswer, it will *not* be able to change its answer.
    # checkAnswer is used to allow your Agent to learn from its incorrect
    # answers; however, your Agent cannot change the answer to a question it
    # has already answered.
    #
    # If your Agent calls checkAnswer during execution of Solve, the answer it
    # returns will be ignored; otherwise, the answer returned at the end of
    # Solve will be taken as your Agent's answer to this problem.
    #
    # Make sure to return your answer *as an integer* at the end of Solve().
    # Returning your answer as a string may cause your program to crash.
    def Solve(self,problem):
        print '\n\nNew Problem',problem.name
        answer = -1
        try:
            if problem.problemType == '3x3':
                if 'Problem E' in problem.name:
                    answer = self.Solve_3x3_E(problem)
                elif 'Problem D' in problem.name:
                    answer = self.Solve_3x3_D(problem)
                elif 'Problem C' in problem.name:
                    answer = self.Solve_3x3_C(problem)
                else:
                    answer = self.Solve_3x3(problem)

            elif problem.problemType == '2x2':
                answer = self.Solve_2x2(problem)
        except Exception as e:
            print "Error occured in this problem",e

        return answer

    def Solve_3x3(self, problem):
        answer = -1
        while True:
            answer = self.check_no_change_horizontal(problem)
            if answer != -1:
                break
            answer = self.check_no_change_vertical(problem)
            if answer != -1:
                break
            answer = self.check_symmetry(problem)
            if answer != -1:
                break
            answer = self.check_diagnol_same(problem)
            if answer != -1:
                break

            #From E
            answer = self.horizontal_union(problem)
            if answer != -1:
                break
            answer = self.horizontal_intersection(problem)
            if answer != -1:
                break
            answer = self.intersection_union_diff(problem)
            if answer != -1:
                break
            answer = self.offset_B_horizontal_difference(problem)
            if answer != -1:
                break
            answer = self.top_A_bottom_B(problem)
            if answer != -1:
                break
            answer = self.top_B_bottom_A(problem)
            if answer != -1:
                break
            answer = self.vertical_union(problem)
            if answer != -1:
                break
            answer = self.vertical_intersection(problem)
            if answer != -1:
                break
            answer = self.rotate_diagnol_check(problem)
            if answer != -1:
                break
            answer = self.flipped_offset_B_horizontal_difference_generic(problem)
            if answer != -1:
                break
            answer = self.flipped_offset_B_horizontal_difference_specific(problem)
            if answer != -1:
                break

            #From D
            answer = self.inner_horizontal_outer_vertical(problem)
            if answer != -1:
                break
            answer = self.inner_vertical_outer_horizontal(problem)
            if answer != -1:
                break
            answer = self.inner_diagnol_outer_horizontal(problem)
            if answer != -1:
                break
            answer = self.inner_diagnol_outer_vertical(problem)
            if answer != -1:
                break
            answer = self.inner_horizontal_outer_diagnol(problem)
            if answer != -1:
                break
            answer = self.inner_vertical_outer_diagnol(problem)
            if answer != -1:
                break
            answer = self.outer_diagnol_inner_cross_diagnol(problem)
            if answer != -1:
                break
            answer = self.inner_diagnol_outer_cross_diagnol(problem)
            if answer != -1:
                break
            answer = self.rotate_diagnol_check(problem)
            if answer != -1:
                break
            answer = self.plus_pattern_cross_diagnol_shape(problem)
            if answer != -1:
                break
            answer = self.cross_diagnol_difference_scaling(problem)
            if answer != -1:
                break

            #From C
            answer = self.check_offset_and_copy(problem,0)
            if answer != -1:
                break
            answer = self.check_object_diff(problem)
            if answer != -1:
                break
            answer = self.check_complex_scaling(problem)
            if answer != -1:
                break
            answer = self.check_roll_mid(problem)
            if answer != -1:
                break


            answer = self.horizontal_union_high_threshold(problem)
            if answer != -1:
                break
            answer = self.check_generic_pix_diff(problem)
            if answer != -1:
                break
            answer = self.check_generic_scaling(problem)
            if answer != -1:
                break
            answer = self.diagnol_diff_high_threshold(problem)
            if answer != -1:
                break
            return -1
        return answer

    def Solve_3x3_C(self, problem):
        answer = -1
        while True:
            answer = self.check_no_change_horizontal(problem)
            if answer != -1:
                break
            answer = self.check_no_change_vertical(problem)
            if answer != -1:
                break
            answer = self.check_symmetry(problem)
            if answer != -1:
                break
            answer = self.check_offset_and_copy(problem,0)
            if answer != -1:
                break
            answer = self.check_object_diff(problem)
            if answer != -1:
                break
            answer = self.check_complex_scaling(problem)
            if answer != -1:
                break
            answer = self.check_roll_mid(problem)
            if answer != -1:
                break
            answer = self.check_min_horizontal_vertical_pix_dif(problem)
            if answer != -1:
                break
            answer = self.check_generic_scaling(problem)
            if answer != -1:
                break
            answer = self.check_generic_pix_diff(problem)
            if answer != -1:
                break
            return -1
        return answer

    def Solve_3x3_D(self, problem):
        answer = -1
        while True:
            answer = self.check_no_change_horizontal(problem)
            if answer != -1:
                break
            answer = self.check_no_change_vertical(problem)
            if answer != -1:
                break
            answer = self.check_symmetry(problem)
            if answer != -1:
                break
            answer = self.check_diagnol_same(problem)
            if answer != -1:
                break
            answer = self.inner_horizontal_outer_vertical(problem)
            if answer != -1:
                break
            answer = self.inner_vertical_outer_horizontal(problem)
            if answer != -1:
                break
            answer = self.inner_diagnol_outer_horizontal(problem)
            if answer != -1:
                break
            answer = self.inner_diagnol_outer_vertical(problem)
            if answer != -1:
                break
            answer = self.inner_horizontal_outer_diagnol(problem)
            if answer != -1:
                break
            answer = self.inner_vertical_outer_diagnol(problem)
            if answer != -1:
                break
            answer = self.outer_diagnol_inner_cross_diagnol(problem)
            if answer != -1:
                break
            answer = self.inner_diagnol_outer_cross_diagnol(problem)
            if answer != -1:
                break
            answer = self.rotate_diagnol_check(problem)
            if answer != -1:
                break
            answer = self.plus_pattern_cross_diagnol_shape(problem)
            if answer != -1:
                break
            answer = self.cross_diagnol_difference_scaling(problem)
            if answer != -1:
                break

            #From E
            answer = self.horizontal_union(problem)
            if answer != -1:
                break
            answer = self.horizontal_intersection(problem)
            if answer != -1:
                break
            answer = self.intersection_union_diff(problem)
            if answer != -1:
                break
            answer = self.offset_B_horizontal_difference(problem)
            if answer != -1:
                break
            answer = self.top_A_bottom_B(problem)
            if answer != -1:
                break
            answer = self.top_B_bottom_A(problem)
            if answer != -1:
                break
            answer = self.vertical_union(problem)
            if answer != -1:
                break
            answer = self.vertical_intersection(problem)
            if answer != -1:
                break
            answer = self.rotate_diagnol_check(problem)
            if answer != -1:
                break
            answer = self.flipped_offset_B_horizontal_difference_generic(problem)
            if answer != -1:
                break

            answer = self.horizontal_union_high_threshold(problem)
            if answer != -1:
                break
            answer = self.check_generic_pix_diff(problem)
            if answer != -1:
                break
            answer = self.check_generic_scaling(problem)
            if answer != -1:
                break
            answer = self.diagnol_diff_high_threshold(problem)
            if answer != -1:
                break
            return -1
        return answer

    def Solve_3x3_E(self, problem):
        answer = -1

        while True:
            answer = self.check_no_change_horizontal(problem)
            if answer != -1:
                break
            answer = self.check_no_change_vertical(problem)
            if answer != -1:
                break
            answer = self.check_symmetry(problem)
            if answer != -1:
                break
            answer = self.check_diagnol_same(problem)
            if answer != -1:
                break
            answer = self.horizontal_union(problem)
            if answer != -1:
                break
            answer = self.horizontal_intersection(problem)
            if answer != -1:
                break
            answer = self.intersection_union_diff(problem)
            if answer != -1:
                break
            answer = self.offset_B_horizontal_difference(problem)
            if answer != -1:
                break
            answer = self.top_A_bottom_B(problem)
            if answer != -1:
                break
            answer = self.top_B_bottom_A(problem)
            if answer != -1:
                break
            answer = self.vertical_union(problem)
            if answer != -1:
                break
            answer = self.vertical_intersection(problem)
            if answer != -1:
                break
            answer = self.rotate_diagnol_check(problem)
            if answer != -1:
                break
            answer = self.flipped_offset_B_horizontal_difference_generic(problem)
            if answer != -1:
                break
            answer = self.flipped_offset_B_horizontal_difference_specific(problem)
            if answer != -1:
                break

            #From D
            answer = self.inner_horizontal_outer_vertical(problem)
            if answer != -1:
                break
            answer = self.inner_vertical_outer_horizontal(problem)
            if answer != -1:
                break
            answer = self.inner_diagnol_outer_horizontal(problem)
            if answer != -1:
                break
            answer = self.inner_diagnol_outer_vertical(problem)
            if answer != -1:
                break
            answer = self.inner_horizontal_outer_diagnol(problem)
            if answer != -1:
                break
            answer = self.inner_vertical_outer_diagnol(problem)
            if answer != -1:
                break
            answer = self.outer_diagnol_inner_cross_diagnol(problem)
            if answer != -1:
                break
            answer = self.inner_diagnol_outer_cross_diagnol(problem)
            if answer != -1:
                break
            answer = self.rotate_diagnol_check(problem)
            if answer != -1:
                break
            answer = self.plus_pattern_cross_diagnol_shape(problem)
            if answer != -1:
                break
            answer = self.cross_diagnol_difference_scaling(problem)
            if answer != -1:
                break

            answer = self.horizontal_union_high_threshold(problem)
            if answer != -1:
                break
            answer = self.check_generic_pix_diff(problem)
            if answer != -1:
                break
            answer = self.check_generic_scaling(problem)
            if answer != -1:
                break
            answer = self.diagnol_diff_high_threshold(problem)
            if answer != -1:
                break
            return -1
        return answer

    def check_diagnol_same(self,problem):
        try:
            print "In check_diagnol_same()"
            imgA = Image.open(problem.figures['A'].visualFilename)
            imgE = Image.open(problem.figures['E'].visualFilename)

            difference = self.get_diff_percentage(imgA,imgE)

            if difference < 3.0:
                final_answer = self.get_answer(imgE,problem)
                print "Final answer is",final_answer
                return final_answer
        except Exception as e:
            print "Some error occured",e
        return -1

    def rotate_diagnol_check(self,problem):
        try:
            print "In rotate_diagnol_check()"
            imgA = Image.open(problem.figures['A'].visualFilename)
            imgA_rotated = imgA.transpose(Image.ROTATE_270)
            imgF = Image.open(problem.figures['F'].visualFilename)
            imgE = Image.open(problem.figures['E'].visualFilename)

            difference = self.get_diff_percentage(imgA_rotated,imgE)

            if difference < 1.0:
                final_answer = -1
                if 'Problem D' in problem.name:
                    final_answer = self.get_answer(imgE.transpose(Image.ROTATE_270),problem,1.0)
                elif 'Problem E' in problem.name:
                    final_answer = self.get_answer(imgF.transpose(Image.ROTATE_270),problem,1.0)
                print "Final answer is",final_answer
                return final_answer
        except Exception as e:
            print "Some error occured",e
        return -1

    def horizontal_union(self,problem):
        try:
            print "In horizontal_union()"
            imgA = Image.open(problem.figures['A'].visualFilename)
            imgB = Image.open(problem.figures['B'].visualFilename)
            imgC = Image.open(problem.figures['C'].visualFilename)

            img_add_A_B = self.get_union(imgA,imgB)
            difference = self.get_diff_percentage(img_add_A_B,imgC)

            if difference < 1.0:
                imgG = Image.open(problem.figures['G'].visualFilename)
                imgH = Image.open(problem.figures['H'].visualFilename)
                final_answer = self.get_answer(self.get_union(imgG,imgH),problem)
                print "Final answer is",final_answer
                return final_answer
        except Exception as e:
            print "Some error occured",e
        return -1

    def horizontal_union_high_threshold(self,problem):
        try:
            print "In horizontal_union_high_threshold()"
            imgA = Image.open(problem.figures['A'].visualFilename)
            imgB = Image.open(problem.figures['B'].visualFilename)
            imgC = Image.open(problem.figures['C'].visualFilename)

            img_add_A_B = self.get_union(imgA,imgB)
            difference = self.get_diff_percentage(img_add_A_B,imgC)

            if difference < 5.0:
                imgG = Image.open(problem.figures['G'].visualFilename)
                imgH = Image.open(problem.figures['H'].visualFilename)
                final_answer = self.get_answer(self.get_union(imgG,imgH),problem)
                print "Final answer is",final_answer
                return final_answer
        except Exception as e:
            print "Some error occured",e
        return -1

    def horizontal_intersection(self,problem):
        try:
            print "In horizontal_intersection()"
            imgA = Image.open(problem.figures['A'].visualFilename)
            imgB = Image.open(problem.figures['B'].visualFilename)
            imgC = Image.open(problem.figures['C'].visualFilename)

            img_add_A_b = self.get_intersection(imgA,imgB)

            difference = self.get_diff_percentage(img_add_A_b,imgC)

            if difference < 1:
                imgG = Image.open(problem.figures['G'].visualFilename)
                imgH = Image.open(problem.figures['H'].visualFilename)
                final_answer = self.get_answer(self.get_intersection(imgG,imgH),problem)
                print "Final answer is",final_answer
                return final_answer
        except Exception as e:
            print "Some error occured",e
        return -1

    def vertical_union(self,problem):
        try:
            print "In vertical_union()"
            imgA = Image.open(problem.figures['A'].visualFilename)
            imgC = Image.open(problem.figures['C'].visualFilename)
            imgD = Image.open(problem.figures['D'].visualFilename)
            imgG = Image.open(problem.figures['G'].visualFilename)
            imgF = Image.open(problem.figures['F'].visualFilename)

            img_add_A_D = self.get_union(imgA,imgD)

            difference = self.get_diff_percentage(img_add_A_D,imgG)
            if difference < 1.0:
                final_answer = self.get_answer(self.get_union(imgC,imgF),problem)
                print "Final answer is",final_answer
                return final_answer
        except Exception as e:
            print "Some error occured",e
        return -1

    def vertical_intersection(self,problem):
        try:
            print "In vertical_intersection()"
            imgA = Image.open(problem.figures['A'].visualFilename)
            imgC = Image.open(problem.figures['C'].visualFilename)
            imgD = Image.open(problem.figures['D'].visualFilename)
            imgG = Image.open(problem.figures['G'].visualFilename)
            imgF = Image.open(problem.figures['F'].visualFilename)

            img_add_A_D = self.get_intersection(imgA,imgD)

            difference = self.get_diff_percentage(img_add_A_D,imgG)
            if difference < 1.0:
                final_answer = self.get_answer(self.get_intersection(imgC,imgF),problem)
                print "Final answer is",final_answer
                return final_answer
        except Exception as e:
            print "Some error occured",e
        return -1


    #Ref E-04
    def offset_B_horizontal_difference(self, problem, image_from_called = None, called = False):

        try:
            print "In offset_B_horizontal_difference()"
            imgA = Image.open(problem.figures['A'].visualFilename)

            if called:
                imgB = image_from_called
            else:
                imgB = Image.open(problem.figures['B'].visualFilename)

            imgC = Image.open(problem.figures['C'].visualFilename)

            offsetA = self.get_offset(imgA)
            left_margin_A = offsetA[0]
            offsetB = self.get_offset(imgB)
            left_margin_B = offsetB[0]
            x_change = left_margin_A-left_margin_B

            imgB_horizontal_offset = ImageChops.offset(imgB,x_change,0)

            imgA_B_difference = ImageChops.difference(imgA,imgB_horizontal_offset)
            imgA_B_difference = ImageChops.invert(imgA_B_difference)

            imgA_B_difference = self.center_align_horizontal(imgA_B_difference)
            difference = self.get_diff_percentage(imgA_B_difference,imgC)

            if difference < 3:
                imgG = Image.open(problem.figures['G'].visualFilename)
                imgH = Image.open(problem.figures['H'].visualFilename)

                if called:
                    imgH = imgH.transpose(Image.FLIP_TOP_BOTTOM)

                offsetG = self.get_offset(imgG)
                left_margin_G = offsetG[0]
                offsetH = self.get_offset(imgH)
                left_margin_H = offsetH[0]
                x_change = left_margin_G-left_margin_H

                imgH_horizontal_offset = ImageChops.offset(imgH,x_change,0)

                imgG_H_difference = ImageChops.difference(imgG,imgH_horizontal_offset)
                imgG_H_difference = ImageChops.invert(imgG_H_difference)

                imgG_H_difference = self.center_align_horizontal(imgG_H_difference)

                final_answer = self.get_answer(imgG_H_difference,problem)
                print "Final answer is",final_answer
                return final_answer
        except Exception as e:
            print "Some error occured",e
        return -1

    #Ref E-06, E-07, E-08
    def intersection_union_diff(self,problem):
        try:
            print "In intersection_union_diff()"
            imgA = Image.open(problem.figures['A'].visualFilename)
            imgB = Image.open(problem.figures['B'].visualFilename)
            imgC = Image.open(problem.figures['C'].visualFilename)

            intersection_A_B = self.get_intersection(imgA,imgB)
            union_A_B = self.get_union(imgA,imgB)
            resultant = ImageChops.difference(union_A_B,intersection_A_B)
            resultant = ImageChops.invert(resultant)

            difference = self.get_diff_percentage(resultant,imgC)
            #print 'The difference found is:',difference

            if difference < 3:
                imgG = Image.open(problem.figures['G'].visualFilename)
                imgH = Image.open(problem.figures['H'].visualFilename)

                intersection_G_H = self.get_intersection(imgG,imgH)
                union_G_H = self.get_union(imgG,imgH)
                resultant = ImageChops.difference(union_G_H,intersection_G_H)
                resultant = ImageChops.invert(resultant)

                final_answer = self.get_answer(resultant,problem)
                print "Final answer is",final_answer
                return final_answer
        except Exception as e:
            print "Some error occured",e
        return -1

    #Ref E-12(but the images are not perfect)
    def flipped_offset_B_horizontal_difference_generic(self, problem):
        print "In flipped_offset_B_horizontal_difference_generic()"
        imgB = Image.open(problem.figures['B'].visualFilename)
        imgB_flipped = imgB.transpose(Image.FLIP_TOP_BOTTOM)
        return self.offset_B_horizontal_difference(problem,imgB_flipped,True)


    #Ref E-12
    def flipped_offset_B_horizontal_difference_specific(self, problem):
        try:
            print "In flipped_offset_B_horizontal_difference_specific()"
            imgA = Image.open(problem.figures['A'].visualFilename)
            imgB = Image.open(problem.figures['B'].visualFilename)
            imgB = imgB.transpose(Image.FLIP_TOP_BOTTOM)
            imgC = Image.open(problem.figures['C'].visualFilename)

            offsetA = self.get_offset(imgA)
            left_margin_A = offsetA[0]
            offsetB = self.get_offset(imgB)
            left_margin_B = offsetB[0]
            x_change = left_margin_A-left_margin_B

            imgB_horizontal_offset = ImageChops.offset(imgB,x_change,0)

            imgA_B_difference = ImageChops.difference(imgA,imgB_horizontal_offset)
            imgA_B_difference = ImageChops.invert(imgA_B_difference)
            #imgA_B_difference.show()

            imgA_B_difference = self.center_align_horizontal(imgA_B_difference)
            #imgA_B_difference.show()

            difference = abs(self.get_pixel_count(imgA_B_difference.convert(mode='L')) - self.get_pixel_count(imgC.convert(mode='L')))
            #print 'Difference here is:',difference ,self.get_pixel_count(imgA_B_difference.convert(mode='L')),self.get_pixel_count(imgC.convert(mode='L'))

            if difference < 70:
                imgG = Image.open(problem.figures['G'].visualFilename)
                imgH = Image.open(problem.figures['H'].visualFilename)
                imgH = imgH.transpose(Image.FLIP_TOP_BOTTOM)

                offsetG = self.get_offset(imgG)
                left_margin_G = offsetG[0]
                offsetH = self.get_offset(imgH)
                left_margin_H = offsetH[0]
                x_change = left_margin_G-left_margin_H

                imgH_horizontal_offset = ImageChops.offset(imgH,x_change,0)

                imgG_H_difference = ImageChops.difference(imgG,imgH_horizontal_offset)
                imgG_H_difference = ImageChops.invert(imgG_H_difference)

                imgG_H_difference = self.center_align_horizontal(imgG_H_difference)

                final_answer = self.get_answer_on_pixel_count(imgG_H_difference,problem)
                print "Final answer is",final_answer
                return final_answer
        except Exception as e:
            print "Some error occured",e
        return -1

    #Ref E-09
    def top_A_bottom_B(self, problem):
        try:
            print "In top_A_bottom_B()"
            imgA = Image.open(problem.figures['A'].visualFilename)
            imgB = Image.open(problem.figures['B'].visualFilename)
            imgC = Image.open(problem.figures['C'].visualFilename)

            top_half = imgA.crop((0,0,imgA.width,imgA.height/2))
            bottom_half = imgB.crop((0,imgB.height/2,imgB.width,imgB.height))

            img_result = imgA.copy()
            img_result.paste(top_half,(0,0,imgA.width,imgA.height/2))
            img_result.paste(bottom_half,(0,imgB.height/2,imgB.width,imgB.height))

            difference = self.get_diff_percentage(img_result,imgC)

            if difference < 1.0:
                imgG = Image.open(problem.figures['G'].visualFilename)
                imgH = Image.open(problem.figures['H'].visualFilename)

                top_half = imgG.crop((0,0,imgG.width,imgG.height/2))
                bottom_half = imgH.crop((0,imgH.height/2,imgH.width,imgH.height))

                img_result = imgG.copy()
                img_result.paste(top_half,(0,0,imgG.width,imgG.height/2))
                img_result.paste(bottom_half,(0,imgH.height/2,imgH.width,imgH.height))

                final_answer = self.get_answer(img_result,problem)
                print "Final answer is",final_answer
                return final_answer
        except Exception as e:
            print "Some error occured",e
        return -1

    def top_B_bottom_A(self, problem):
        try:
            print "In top_B_bottom_A()"
            imgA = Image.open(problem.figures['A'].visualFilename)
            imgB = Image.open(problem.figures['B'].visualFilename)
            imgC = Image.open(problem.figures['C'].visualFilename)

            top_half = imgB.crop((0,0,imgB.width,imgB.height/2))
            bottom_half = imgA.crop((0,imgA.height/2,imgA.width,imgA.height))

            img_result = imgA.copy()
            img_result.paste(top_half,(0,0,imgA.width,imgA.height/2))
            img_result.paste(bottom_half,(0,imgB.height/2,imgB.width,imgB.height))

            difference = self.get_diff_percentage(img_result,imgC)

            if difference < 1.0:
                imgG = Image.open(problem.figures['G'].visualFilename)
                imgH = Image.open(problem.figures['H'].visualFilename)

                top_half = imgH.crop((0,0,imgG.width,imgG.height/2))
                bottom_half = imgG.crop((0,imgH.height/2,imgH.width,imgH.height))

                img_result = imgG.copy()
                img_result.paste(top_half,(0,0,imgG.width,imgG.height/2))
                img_result.paste(bottom_half,(0,imgH.height/2,imgH.width,imgH.height))

                final_answer = self.get_answer(img_result,problem)
                print "Final answer is",final_answer
                return final_answer
        except Exception as e:
            print "Some error occured",e
        return -1

    #Ref D-04,D-05
    def inner_horizontal_outer_vertical(self,problem):
        try:
            print "In inner_horizontal_outer_vertical()"
            imgA = Image.open(problem.figures['A'].visualFilename)
            imgC = Image.open(problem.figures['C'].visualFilename)
            imgG = Image.open(problem.figures['G'].visualFilename)

            inner_A = self.get_inner_image(imgA)
            inner_C = self.get_inner_image(imgC)
            outer_A = self.get_outer_image(imgA)
            outer_G = self.get_outer_image(imgG)

            diff1 = self.get_diff_percentage(inner_A,inner_C)
            diff2 = self.get_diff_percentage(outer_A,outer_G)

            if (diff1+diff2) < 1.0:
                img1 = self.get_inner_image(imgG)
                img2 = self.get_outer_image(imgC)
                result = self.get_union(img1,img2)
                final_answer = self.get_answer(result,problem,0.5)
                print "Final answer is",final_answer
                return final_answer
        except Exception as e:
            print "Some error occured",e
        return -1

    def inner_vertical_outer_horizontal(self,problem):
        try:
            print "In inner_vertical_outer_horizontal()"
            imgA = Image.open(problem.figures['A'].visualFilename)
            imgC = Image.open(problem.figures['C'].visualFilename)
            imgG = Image.open(problem.figures['G'].visualFilename)

            inner_A = self.get_inner_image(imgA)
            inner_G = self.get_inner_image(imgG)
            outer_A = self.get_outer_image(imgA)
            outer_C = self.get_outer_image(imgC)

            diff1 = self.get_diff_percentage(inner_A,inner_G)
            diff2 = self.get_diff_percentage(outer_A,outer_C)

            if (diff1+diff2) < 1.0:
                img1 = self.get_inner_image(imgC)
                img2 = self.get_outer_image(imgG)
                result = self.get_union(img1,img2)
                final_answer = self.get_answer(result,problem,0.5)
                print "Final answer is",final_answer
                return final_answer
        except Exception as e:
            print "Some error occured",e
        return -1

    #Ref D-06
    def inner_diagnol_outer_horizontal(self,problem):
        try:
            print "In inner_diagnol_outer_horizontal()"
            imgA = Image.open(problem.figures['A'].visualFilename)
            imgC = Image.open(problem.figures['C'].visualFilename)
            imgE = Image.open(problem.figures['E'].visualFilename)
            imgG = Image.open(problem.figures['G'].visualFilename)

            inner_A = self.get_inner_image(imgA)
            inner_E = self.get_inner_image(imgE)
            outer_A = self.get_outer_image(imgA)
            outer_C = self.get_outer_image(imgC)

            diff1 = self.get_diff_percentage(inner_A,inner_E)
            diff2 = self.get_diff_percentage(outer_A,outer_C)

            if (diff1+diff2) < 1.0:
                img1 = self.get_inner_image(imgA)
                img2 = self.get_outer_image(imgG)
                result = self.get_union(img1,img2)
                final_answer = self.get_answer(result,problem,0.5)
                print "Final answer is",final_answer
                return final_answer
        except Exception as e:
            print "Some error occured",e
        return -1

    def inner_diagnol_outer_vertical(self,problem):
        try:
            print "In inner_diagnol_outer_vertical()"
            imgA = Image.open(problem.figures['A'].visualFilename)
            imgC = Image.open(problem.figures['C'].visualFilename)
            imgE = Image.open(problem.figures['E'].visualFilename)
            imgG = Image.open(problem.figures['G'].visualFilename)

            inner_A = self.get_inner_image(imgA)
            inner_E = self.get_inner_image(imgE)
            outer_A = self.get_outer_image(imgA)
            outer_G = self.get_outer_image(imgG)

            diff1 = self.get_diff_percentage(inner_A,inner_E)
            diff2 = self.get_diff_percentage(outer_A,outer_G)

            if (diff1+diff2) < 1.0:
                img1 = self.get_inner_image(imgA)
                img2 = self.get_outer_image(imgC)
                result = self.get_union(img1,img2)
                final_answer = self.get_answer(result,problem,0.5)
                print "Final answer is",final_answer
                return final_answer
        except Exception as e:
            print "Some error occured",e
        return -1

    def inner_horizontal_outer_diagnol(self,problem):
        try:
            print "In inner_horizontal_outer_diagnol()"
            imgA = Image.open(problem.figures['A'].visualFilename)
            imgC = Image.open(problem.figures['C'].visualFilename)
            imgE = Image.open(problem.figures['E'].visualFilename)
            imgG = Image.open(problem.figures['G'].visualFilename)

            inner_A = self.get_inner_image(imgA)
            outer_A = self.get_outer_image(imgA)
            inner_C = self.get_inner_image(imgC)
            outer_E = self.get_outer_image(imgE)

            diff1 = self.get_diff_percentage(inner_A,inner_C)
            diff2 = self.get_diff_percentage(outer_A,outer_E)

            if (diff1+diff2) < 1.0:
                img1 = self.get_inner_image(imgG)
                img2 = self.get_outer_image(imgA)
                result = self.get_union(img1,img2)
                final_answer = self.get_answer(result,problem,0.5)
                print "Final answer is",final_answer
                return final_answer
        except Exception as e:
            print "Some error occured",e
        return -1

    def inner_vertical_outer_diagnol(self,problem):
        try:
            print "In inner_vertical_outer_diagnol()"
            imgA = Image.open(problem.figures['A'].visualFilename)
            imgC = Image.open(problem.figures['C'].visualFilename)
            imgE = Image.open(problem.figures['E'].visualFilename)
            imgG = Image.open(problem.figures['G'].visualFilename)

            inner_A = self.get_inner_image(imgA)
            outer_A = self.get_outer_image(imgA)
            inner_G = self.get_inner_image(imgG)
            outer_E = self.get_outer_image(imgE)

            diff1 = self.get_diff_percentage(inner_A,inner_G)
            diff2 = self.get_diff_percentage(outer_A,outer_E)

            if (diff1+diff2) < 1.0:
                img1 = self.get_inner_image(imgC)
                img2 = self.get_outer_image(imgA)
                result = self.get_union(img1,img2)
                final_answer = self.get_answer(result,problem,0.5)
                print "Final answer is",final_answer
                return final_answer
        except Exception as e:
            print "Some error occured",e
        return -1

    #Ref D-07
    def outer_diagnol_inner_cross_diagnol(self,problem):
        try:
            print "In outer_diagnol_inner_cross_diagnol()"
            imgA = Image.open(problem.figures['A'].visualFilename)
            imgB = Image.open(problem.figures['B'].visualFilename)
            imgD = Image.open(problem.figures['D'].visualFilename)
            imgE = Image.open(problem.figures['E'].visualFilename)


            inner_B = self.get_inner_image(imgB)
            inner_D = self.get_inner_image(imgD)
            outer_A = self.get_outer_image(imgA)
            outer_E = self.get_outer_image(imgE)

            diff1 = self.get_diff_percentage(inner_B,inner_D)
            diff2 = self.get_diff_percentage(outer_A,outer_E)

            #print diff1,diff2

            if (diff1+diff2) < 1.0:
                img1 = self.get_inner_image(imgB)
                img2 = self.get_outer_image(imgA)
                result = self.get_union(img1,img2)
                final_answer = self.get_answer(result,problem,1.0)
                print "Final answer is",final_answer
                return final_answer
        except Exception as e:
            print "Some error occured",e
        return -1

    #Ref D-10
    def inner_diagnol_outer_cross_diagnol(self,problem):
        try:
            print "In inner_diagnol_outer_cross_diagnol()"
            imgA = Image.open(problem.figures['A'].visualFilename)
            imgB = Image.open(problem.figures['B'].visualFilename)
            imgD = Image.open(problem.figures['D'].visualFilename)
            imgE = Image.open(problem.figures['E'].visualFilename)


            outer_B = self.get_outer_image(imgB)
            outer_D = self.get_outer_image(imgD)
            inner_A = self.get_inner_image(imgA)
            inner_E = self.get_inner_image(imgE)

            diff1 = self.get_diff_percentage(inner_A,inner_E)
            diff2 = self.get_diff_percentage(outer_B,outer_D)

            if (diff1+diff2) < 1.0:
                img1 = self.get_inner_image(imgA)
                img2 = self.get_outer_image(imgB)
                result = self.get_union(img1,img2)

                final_answer = self.get_answer(result,problem,1.0)
                print "Final answer is",final_answer
                return final_answer
        except Exception as e:
            print "Some error occured",e
        return -1

    #Ref D-12
    def diagnol_diff_high_threshold(self, problem):
        try:
            flag = False
            print "In diagnol_diff_high_threshold()"
            imgA = Image.open(problem.figures['A'].visualFilename)
            imgA_flipped = imgA.transpose(Image.FLIP_LEFT_RIGHT)
            #imgA.show()
            imgE = Image.open(problem.figures['E'].visualFilename)

            difference = self.get_diff_percentage(imgA_flipped,imgE)
            #print 'inside this method',difference

            if difference >= 6.0:
                difference = self.get_diff_percentage(imgA,imgE)
                flag = True


            if difference < 6.0:
                final_answer = self.get_answer(imgE, problem, 1.0)
                if flag:
                    final_answer = self.get_answer(imgE, problem, 1.0)
                print "Final answer is",final_answer
                return final_answer
        except Exception as e:
            print "Some error occured",e
        return -1

    #Ref D-08
    def cross_diagnol_difference_scaling(self, problem):
        try:
            print "In cross_diagnol_difference_scaling()"
            imgA = Image.open(problem.figures['A'].visualFilename)
            imgF = Image.open(problem.figures['F'].visualFilename)
            imgH = Image.open(problem.figures['H'].visualFilename)

            offsetF = self.get_offset(imgF)
            offsetH = self.get_offset(imgH)

            lengthF = offsetF[2] - offsetF[0]
            widthF = offsetF[3] - offsetF[1]
            lengthH = offsetH[2] - offsetH[0]
            widthH = offsetH[3] - offsetH[1]

            scaleX = lengthH/float(lengthF)
            scaleY = widthH/float(widthF)

            scaleTuple = int(scaleX*imgF.size[0]),int(scaleY*imgF.size[1])

            imgF_resize = imgF.resize(scaleTuple)

            new_width = imgF_resize.size[0]
            new_height = imgF_resize.size[1]

            left_margin = (new_width - imgF.size[0])/2
            right_margin = new_width - left_margin
            top_margin = (new_height - imgF.size[1])/2
            bottom_margin = new_height - top_margin
            crop_tuple = left_margin, top_margin, right_margin, bottom_margin
            cropped_imgF = imgF_resize.crop(crop_tuple)

            diff_F_H = ImageChops.invert(ImageChops.difference(cropped_imgF,imgH))

            difference = self.get_diff_percentage(imgA,diff_F_H)

            if difference < 4.0:
                imgB = Image.open(problem.figures['B'].visualFilename)
                imgB_resize = imgB.resize(scaleTuple)
                cropped_imgB = imgB_resize.crop(crop_tuple)
                imgD = Image.open(problem.figures['D'].visualFilename)

                result = ImageChops.invert(ImageChops.difference(cropped_imgB,imgD))
                #result.show()

                final_answer = self.get_answer(result,problem)
                print "Final Answer is",final_answer
                return final_answer
        except Exception as e:
            print "Some error occured",e
        return -1

    #Ref D-09
    def plus_pattern_cross_diagnol_shape(self, problem):
        try:
            print "In plus_pattern_cross_diagnol_shape()"
            imgA = Image.open(problem.figures['A'].visualFilename)
            imgF = Image.open(problem.figures['F'].visualFilename)
            imgH = Image.open(problem.figures['H'].visualFilename)

            add_A_F = self.get_union(imgA,imgF)

            difference = self.get_diff_percentage(add_A_F,imgH)

            if difference < 2.0:
                imgB = Image.open(problem.figures['B'].visualFilename)
                imgD = Image.open(problem.figures['D'].visualFilename)

                intersection_B_D = self.get_intersection(imgD,imgB)

                result = intersection_B_D.transpose(Image.ROTATE_90)

                final_answer = self.get_answer(result,problem)
                print "Final answer is",final_answer
                return final_answer
        except Exception as e:
            print "Some error occured",e
        return -1

    #These methods will return BW images - So make sure you convert everything else
    def get_inner_image(self,img):
        crop_tuple = (int(0.25*img.width),int(0.25*img.height),int(0.75*img.width),int(0.75*img.height))
        inner_part = img.crop(crop_tuple)

        #Creating a blank image
        img_blank = ImageChops.invert(ImageChops.difference(img,img))
        img_blank.paste(inner_part,(int(0.25*img.width),int(0.25*img.height)))
        img_blank_BW = img_blank.convert(mode='L')
        #img_blank_BW.show()
        return img_blank_BW

    def get_outer_image(self,img):
        img_BW = img.convert(mode='L')
        img_inner = self.get_inner_image(img)
        outer_part = ImageChops.invert(ImageChops.difference(img_inner,img_BW))
        #outer_part.show()
        return outer_part

    def center_align_horizontal(self,img):
        img_offset = self.get_offset(img)
        left_margin = img_offset[0]
        right_margin = img.width - img_offset[2]

        offset_difference = left_margin - right_margin
        new_left_margin = left_margin - offset_difference/2
        final_offset_value = new_left_margin - left_margin

        return ImageChops.offset(img,final_offset_value,0)

    def center_align_vertical(self,img):
        img_offset = self.get_offset(img)
        top_margin = img_offset[1]
        bottom_margin = img.width - img_offset[3]

        offset_difference = top_margin - bottom_margin
        new_left_margin = top_margin - offset_difference/2
        final_offset_value = new_left_margin - top_margin

        return ImageChops.offset(img,0,final_offset_value)


    #ProJect-2 Functions
    def check_no_change_horizontal(self,problem):
        try:
            print "In check_no_change_horizontal()"
            imgA = Image.open(problem.figures['A'].visualFilename)
            imgC = Image.open(problem.figures['C'].visualFilename)

            difference = self.get_diff_percentage(imgA,imgC)

            if difference < 3.5:
                imgG = Image.open(problem.figures['G'].visualFilename)
                final_answer = self.get_answer(imgG,problem,0.1)
                print "Final answer is",final_answer
                return final_answer
        except Exception as e:
            print "Some error occured",e
        return -1

    def check_no_change_vertical(self,problem):
        try:
            print "In check_no_change_horizontal()"
            imgA = Image.open(problem.figures['A'].visualFilename)
            imgC = Image.open(problem.figures['C'].visualFilename)
            imgG = Image.open(problem.figures['G'].visualFilename)

            difference = self.get_diff_percentage(imgA,imgG)

            if difference < 1.0:
                final_answer = self.get_answer(imgC,problem,0.1)
                print "Final answer is",final_answer
                return final_answer
        except Exception as e:
            print "Some error occured",e
        return -1

    #Flip Img A and check in horizontal, vertical and diagnol directions
    def check_symmetry(self, problem):
        try:
            print "In check_symmetry()"
            imgA = Image.open(problem.figures['A'].visualFilename)
            imgA_flip_right_left = imgA.transpose(Image.FLIP_LEFT_RIGHT)
            imgC = Image.open(problem.figures['C'].visualFilename)
            imgE = Image.open(problem.figures['E'].visualFilename)
            imgG = Image.open(problem.figures['G'].visualFilename)
            difference = self.get_diff_percentage(imgA_flip_right_left,imgC)

            if difference < 1.0:
                imgG = Image.open(problem.figures['G'].visualFilename)
                imgG_flip = imgG.transpose(Image.FLIP_LEFT_RIGHT)
                final_answer = self.get_answer(imgG_flip,problem)
                print "Final answer is",final_answer
                return final_answer

            imgA_flip_top_bottom = imgA.transpose(Image.FLIP_TOP_BOTTOM)
            difference = self.get_diff_percentage(imgA_flip_top_bottom,imgC)

            if difference < 1.0:
                imgG = Image.open(problem.figures['G'].visualFilename)
                imgG_flip = imgG.transpose(Image.FLIP_TOP_BOTTOM)
                final_answer = self.get_answer(imgG_flip,problem)
                print "Final answer is",final_answer
                return final_answer

            difference = self.get_diff_percentage(imgA_flip_right_left,imgG)

            if difference < 1.0:
                imgC_flip = imgC.transpose(Image.FLIP_LEFT_RIGHT)
                final_answer = self.get_answer(imgC_flip,problem)
                print "Final answer is",final_answer
                return final_answer

            difference = self.get_diff_percentage(imgA_flip_top_bottom,imgG)

            if difference < 1.0:
                imgC_flip = imgC.transpose(Image.FLIP_TOP_BOTTOM)
                final_answer = self.get_answer(imgC_flip,problem)
                print "Final answer is",final_answer
                return final_answer

        except Exception as e:
            print "Some error occured",e
        return -1

    def check_object_diff(self,problem):
        try:
            print "In check_object_diff()"
            imgA = Image.open(problem.figures['A'].visualFilename)
            imgC = Image.open(problem.figures['C'].visualFilename)
            imgG = Image.open(problem.figures['G'].visualFilename)

            difference_img = ImageChops.difference(imgA,imgC)
            difference_img = ImageChops.invert(difference_img)
            imgA_C = self.get_union(difference_img,imgA)
            difference = self.get_diff_percentage(imgA_C,imgC)

            if difference < 1:
                difference_with_G = self.get_diff_percentage(imgA_C,imgG)
                if difference_with_G < 1:
                    return -1
                imgG_res = self.get_union(imgG,difference_img)

                answer_choice = self.get_answer(imgG_res,problem,2)
                print "Final answer is",answer_choice
                return answer_choice
        except Exception as e:
            print "Some error occured",e
        return -1

    def check_offset_and_copy(self, problem, count):
        try:
            if count == 1:
                print "In check_offset_and_copy() - recursed"
            else:
                print "In check_offset_and_copy()"
            flag = count
            imgA = Image.open(problem.figures['A'].visualFilename)
            offsetA = self.get_offset(imgA)

            initial_a_x1 = offsetA[0]
            initial_a_y1 = offsetA[1]
            initial_a_x2 = offsetA[2]
            initial_a_y2 = offsetA[3]

            imgC = Image.open(problem.figures['C'].visualFilename)
            offsetC = self.get_offset(imgA)
            offsetC = self.get_offset(imgC)

            initial_c_x1 = offsetC[0]
            initial_c_y1 = offsetC[1]
            initial_c_x2 = offsetC[2]
            initial_c_y2 = offsetC[3]

            x_change1 = initial_c_x1 - initial_a_x1
            y_change1 = initial_c_y1 - initial_a_y1
            x_change2 = initial_c_x2 - initial_a_x2
            y_change2 = initial_c_y2 - initial_a_y2

            imgA_to_left = ImageChops.offset(imgA,x_change1,y_change1)

            imgA_to_right = ImageChops.offset(imgA,x_change2,y_change2)

            imgA_overlap = self.get_union(imgA_to_left,imgA_to_right)
            if flag == 0:
                imgA_overlap = self.get_union(imgA_overlap,imgA)

            difference = self.get_diff_percentage(imgC, imgA_overlap)

            if difference < 4:
                imgG = Image.open(problem.figures['G'].visualFilename)
                imgG_to_left = ImageChops.offset(imgG,x_change1,y_change1)
                imgG_to_right = ImageChops.offset(imgG,x_change2,y_change2)

                imgG_overlap = self.get_union(imgG_to_left,imgG_to_right)
                if flag == 0:
                    imgG_overlap = self.get_union(imgG_overlap,imgG)

                answer_choice = self.get_answer(imgG_overlap, problem)
                return answer_choice
            elif flag == 0:
                answer_choice = self.check_offset_and_copy(problem,1)
                print "Final answer is",answer_choice
                return  answer_choice
        except Exception as e:
            print "Some error occured",e
        return -1

    def check_complex_scaling(self, problem):
        try:
            print "In check_complex_scaling()"
            imgA = Image.open(problem.figures['A'].visualFilename)
            imgB = Image.open(problem.figures['B'].visualFilename)
            imgC = Image.open(problem.figures['C'].visualFilename)

            imgA_BW = imgA.convert(mode='L')
            imgA_inv = ImageChops.invert(imgA_BW)

            offsetA = imgA_inv.getbbox()

            imgC_BW = imgC.convert(mode='L')
            imgC_inv = ImageChops.invert(imgC_BW)
            offsetC = imgC_inv.getbbox()

            imgB_BW = imgB.convert(mode='L')
            imgB_inv = ImageChops.invert(imgB_BW)
            offsetB = imgB_inv.getbbox()

            lengthA = offsetA[2] - offsetA[0]
            widthA = offsetA[3] - offsetA[1]
            lengthB = offsetB[2] - offsetB[0]
            widthB = offsetB[3] - offsetB[1]

            scaleXB = lengthB/float(lengthA)
            scaleYB = widthB/float(widthA)

            lengthC = offsetC[2] - offsetC[0]
            widthC = offsetC[3] - offsetC[1]

            scaleXC = lengthC/float(lengthB)
            scaleYC = widthC/float(widthB)

            scaleTuple = int(scaleXB*scaleXC*imgA.size[0]),int(scaleYB*scaleYC*imgA.size[1])

            imgAdifC = ImageChops.difference(imgA,imgC)
            imgAdifC = ImageChops.invert(imgAdifC)

            imgAintersectC = self.get_intersection(imgAdifC, imgA)

            imgAintersectC_resize = imgAintersectC.resize(scaleTuple)

            new_width = imgAintersectC_resize.size[0]
            new_height = imgAintersectC_resize.size[1]

            left_margin = (new_width - imgA.size[0])/2
            right_margin = new_width - left_margin
            top_margin = (new_height - imgA.size[1])/2
            bottom_margin = new_height - top_margin
            crop_tuple = left_margin, top_margin, right_margin, bottom_margin
            cropped_imgA = imgAintersectC_resize.crop(crop_tuple)

            intersect_inner = self.get_intersection(imgA,imgC)

            final_img = self.get_union(intersect_inner, cropped_imgA)

            difference = self.get_diff_percentage(final_img, imgC)

            scaleTuple_res = int(1.45*imgA.size[0]),int(1.45*imgA.size[1])
            if difference<6:
                print difference
                imgG = Image.open(problem.figures['G'].visualFilename)
                imgGdifC = ImageChops.difference(imgG,imgA)
                imgGdifC = ImageChops.invert(imgGdifC)
                imgGintersectC = self.get_intersection(imgGdifC, imgG)
                imgGintersectC_resize = imgGintersectC.resize(scaleTuple_res)

                new_width = imgGintersectC_resize.size[0]
                new_height = imgGintersectC_resize.size[1]

                left_margin = (new_width - imgA.size[0])/2
                right_margin = new_width - left_margin
                top_margin = (new_height - imgA.size[1])/2
                bottom_margin = new_height - top_margin
                crop_tuple = left_margin, top_margin, right_margin, bottom_margin

                cropped_imgG = imgGintersectC_resize.crop(crop_tuple)
                result_img = self.get_union(intersect_inner, cropped_imgG)

                final_answer = self.get_answer(result_img,problem)
                print "FInal answer is",final_answer
                return final_answer

        except Exception as e:
            print "Some error occured",e
        return -1

    #Roll image by cutting in the middle
    def check_roll_mid(self, problem):
        print "In check_roll_mid()"
        imgA = Image.open(problem.figures['A'].visualFilename)
        imgC = Image.open(problem.figures['C'].visualFilename)
        imgG = Image.open(problem.figures['G'].visualFilename)

        width, height = imgA.size

        left_half = imgA.crop((0, 0, width/2, height))
        right_half = imgA.crop((width/2,0,width,height))
        img_result = imgA.copy()
        img_result_offset = imgA.copy()

        img_result.paste(right_half,(0,0,width/2,height))
        img_result.paste(left_half,(width/2,0,width,height))

        difference = self.get_diff_percentage(img_result,imgC)

        if difference >= 1.5:
            img_result_offset.paste(right_half,(5,0,width/2+5,height))
            img_result_offset.paste(left_half,(width/2-5,0,width-5,height))
            difference = self.get_diff_percentage(img_result_offset,imgC)

        if difference < 1.5:
            left_half = imgG.crop((0, 0, width/2, height))

            right_half = imgG.crop((width/2,0,width,height))

            img_result_rep = imgG.copy()

            img_result_rep.paste(right_half,(0,0,width/2,height))
            img_result_rep.paste(left_half,(width/2,0,width,height))

            answer_choice = self.get_answer(img_result_rep,problem)
            print "Final answer is",answer_choice
            return answer_choice
        return -1

    def check_min_horizontal_vertical_pix_dif(self,problem):
        try:
            print "In check_min_horizontal_vertical_pix_dif()"
            imgC = Image.open(problem.figures['C'].visualFilename)
            imgF = Image.open(problem.figures['F'].visualFilename)
            imgG = Image.open(problem.figures['G'].visualFilename)
            imgH = Image.open(problem.figures['H'].visualFilename)

            imgC_BW = imgC.convert(mode='L')
            c_pixel_count = self.get_pixel_count(imgC_BW)

            imgF_BW = imgF.convert(mode='L')
            f_pixel_count = self.get_pixel_count(imgF_BW)

            imgG_BW = imgG.convert(mode='L')
            g_pixel_count = self.get_pixel_count(imgG_BW)

            imgH_BW = imgH.convert(mode='L')
            h_pixel_count = self.get_pixel_count(imgH_BW)

            difference_C_F = c_pixel_count - f_pixel_count
            difference_G_H = g_pixel_count - h_pixel_count

            mean_difference = (difference_C_F+difference_G_H)/2

            final_answer = self.get_answer_for_pix(problem,f_pixel_count,mean_difference,150)
            print "Final answer is",final_answer
            return final_answer

        except Exception as e:
            print "Some error occured",e

        return -1

    def check_generic_scaling(self, problem):
        try:
            print "In check_generic_scaling()"
            imgA = Image.open(problem.figures['A'].visualFilename)
            imgC = Image.open(problem.figures['C'].visualFilename)

            offsetA = self.get_offset(imgA)
            offsetC = self.get_offset(imgC)

            lengthA = offsetA[2] - offsetA[0]
            widthA = offsetA[3] - offsetA[1]
            lengthC = offsetC[2] - offsetC[0]
            widthC = offsetC[3] - offsetC[1]

            scaleXC = lengthC/float(lengthA)
            scaleYC = widthC/float(widthA)

            scaleTuple = int(scaleXC*imgA.size[0]),int(scaleYC*imgA.size[1])

            imgA_resize = imgA.resize(scaleTuple)

            new_width = imgA_resize.size[0]
            new_height = imgA_resize.size[1]

            left_margin = (new_width - imgA.size[0])/2
            right_margin = new_width - left_margin
            top_margin = (new_height - imgA.size[1])/2
            bottom_margin = new_height - top_margin
            crop_tuple = left_margin, top_margin, right_margin, bottom_margin
            cropped_imgA = imgA_resize.crop(crop_tuple)

            difference = self.get_diff_percentage(cropped_imgA,imgC)

            if difference < 5:
                imgG = Image.open(problem.figures['G'].visualFilename)
                imgG_resize = imgG.resize(scaleTuple)
                cropped_imgG = imgG_resize.crop(crop_tuple)

                answer = self.get_answer(cropped_imgG,problem,10)
                print "Final Answer is",answer
                return  answer

        except Exception as e:
            print "Some error occured",e

        return -1

    def check_generic_pix_diff(self, problem):
        try:
            print "In check_generic_pix_diff()"
            #if the ratio of pixels changing from A to B to C is same as that from D to E to F then the same will hold for last row otherwise try vertical
            imgA = Image.open(problem.figures['A'].visualFilename)
            imgB = Image.open(problem.figures['B'].visualFilename)
            imgC = Image.open(problem.figures['C'].visualFilename)
            imgD = Image.open(problem.figures['D'].visualFilename)
            imgE = Image.open(problem.figures['E'].visualFilename)
            imgF = Image.open(problem.figures['F'].visualFilename)
            imgG = Image.open(problem.figures['G'].visualFilename)
            imgH = Image.open(problem.figures['H'].visualFilename)

            imgA = imgA.convert(mode='L')
            imgB = imgB.convert(mode='L')
            imgC = imgC.convert(mode='L')
            imgD = imgD.convert(mode='L')
            imgE = imgE.convert(mode='L')
            imgF = imgF.convert(mode='L')
            imgG = imgG.convert(mode='L')
            imgH = imgH.convert(mode='L')

            pix_a = self.get_pixel_count(imgA)
            pix_b = self.get_pixel_count(imgB)
            pix_c = self.get_pixel_count(imgC)
            pix_d = self.get_pixel_count(imgD)
            pix_e = self.get_pixel_count(imgE)
            pix_f = self.get_pixel_count(imgF)
            pix_g = self.get_pixel_count(imgG)
            pix_h = self.get_pixel_count(imgH)

            dif_a_b = pix_a - pix_b
            dif_b_c = pix_b - pix_c
            dif_d_e = pix_d - pix_e
            dif_e_f = pix_e - pix_f
            dif_g_h = pix_g - pix_h

            if dif_b_c == 0:
                return self.get_answer_for_pix(problem,pix_h,0,150)

            ratio_row1 = dif_a_b/float(dif_b_c)
            ratio_row2 = dif_d_e/float(dif_e_f)


            if abs(ratio_row1 - ratio_row2) < 0.2:
                #There is a horizontal pattern
                res_dif = dif_g_h/float(ratio_row1)
                final_answer = self.get_answer_for_pix(problem,pix_h,res_dif,150)
                return final_answer
            else:
                #check for a vertical pattern
                dif_a_d = pix_a - pix_d
                dif_d_g = pix_d - pix_g
                dif_b_e = pix_b - pix_e
                dif_e_h = pix_e - pix_h

                if dif_d_g == 0:
                    return self.get_answer_for_pix(problem,pix_f,0,150)

                ratio_col1 = dif_a_d/float(dif_d_g)
                ratio_col2 = dif_b_e/float(dif_e_h)

                if abs(ratio_col1-ratio_col2) < 0.2:
                    res_dif = dif_e_f/float(ratio_col1)
                    final_answer = self.get_answer_for_pix(problem,pix_f,res_dif,150)
                    print "Final answer is",final_answer
                    return final_answer
        except Exception as e:
            print "Some error occured",e

        return -1

    def get_diff_percentage(self, imgA, imgB):
        pairs = izip(imgA.getdata(), imgB.getdata())
        if len(imgA.getbands()) == 1:
            # for gray-scale images
            dif = sum(abs(p1-p2) for p1,p2 in pairs)
        else:
            dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))

        ncomponents = imgA.size[0] * imgA.size[1] * 3
        return (dif / 255.0 * 100) / ncomponents

    def get_answer(self, result_rep, problem, threshold = 100.0):
        list_result = []
        final_answer = -1
        for i in range(1,9):
            i = str(i)
            cur_result = Image.open(problem.figures[i].visualFilename)

            #Do all operations on BW images (Safety purposes)
            result_rep_BW = result_rep.convert(mode='L')
            cur_result_BW = cur_result.convert(mode='L')

            cur_diff = self.get_diff_percentage(result_rep_BW,cur_result_BW)
            list_result.append(cur_diff)

        #print 'The list in get_answer is:',list_result

        if min(list_result) < threshold:
            final_answer = list_result.index(min(list_result)) + 1
        return final_answer

    def get_answer_on_pixel_count(self, result_rep, problem, threshold = 100.0):
        list_result = []
        final_answer = -1
        for i in range(1,9):
            i = str(i)
            cur_result = Image.open(problem.figures[i].visualFilename)

            #Do all operations on BW images (Safety purposes)
            result_rep_BW = result_rep.convert(mode='L')
            cur_result_BW = cur_result.convert(mode='L')

            cur_diff = abs(self.get_pixel_count(result_rep_BW) - self.get_pixel_count(cur_result_BW))
            list_result.append(cur_diff)

        #print 'The list in get_answer is:',list_result
        if min(list_result) < threshold:
            final_answer = list_result.index(min(list_result)) + 1
        return final_answer

    def get_pixel_count(self, image):
        count = 0
        figureLoaded = image.load()
        for i in range(0, image.size[0]):
            for j in range(0, image.size[1]):
                thisPixel = figureLoaded[i, j]
                if thisPixel == 0:
                    count += 1
        return count

    def get_union(self,img1,img2):
        img_result = ImageChops.darker(img1,img2)
        return img_result

    def get_intersection(self,img1,img2):
        img_result = ImageChops.lighter(img1,img2)
        return img_result

    def get_offset(self, img1):
        img1_BW = img1.convert(mode='L')
        img1_inv = ImageChops.invert(img1_BW)
        return img1_inv.getbbox()

    def get_answer_for_pix(self,problem,img_pix,mean_difference,threshold):
        list_differences=[]
        final_answer = -1
        for i in range(1,9):
            i = str(i)
            cur_result = Image.open(problem.figures[i].visualFilename)
            cur_result_BW = cur_result.convert(mode= 'L')
            cur_pixel_count = self.get_pixel_count(cur_result_BW)
            cur_dif = img_pix - cur_pixel_count
            cur_dif_closest = abs(cur_dif-mean_difference)
            list_differences.append(cur_dif_closest)

        if min(list_differences) < threshold:
            final_answer = list_differences.index(min(list_differences)) + 1

        return final_answer

    #Code for 2x2 Matrix solving
    def Solve_2x2(self,problem):
        try:
            print "\n\n\n\n\nThis is a new Problem: ",problem

            i=0
            trans = {}

            aNoOfObjs = len(problem.figures['B'].objects)
            bNoOfObjs = len(problem.figures['B'].objects)

            #Transformation from A->B
            for objs in sorted(problem.figures['A'].objects):
                i += 1
                trans[i] = {}

                print "Start finding corr obj for",objs
                corr_obj = self.getCorrObj(problem.figures['A'].objects[objs], problem.figures['B'])
                print "Return of finding corr obj",corr_obj

                if corr_obj is None:
                    corr_obj = chr(ord(objs)+len(problem.figures['A'].objects))

                if not (problem.figures['B'].objects.has_key(corr_obj)):
                    print "The object "+corr_obj+" has got deleted"
                    trans[i] = 'delete'
                    print trans
                    continue

                print "Object in for loop:",objs
                print "The corresponding object is:",corr_obj

                print "Start creating transformation for ",objs, corr_obj

                for attr in problem.figures['A'].objects[objs].attributes:
                    if not (problem.figures['B'].objects[corr_obj].attributes.has_key(attr)):
                        trans[i][attr] = 'delete'
                        continue

                    attrA = problem.figures['A'].objects[objs].attributes[attr]
                    attrB = problem.figures['B'].objects[corr_obj].attributes[attr]
                    if attrA == attrB:
                        print "Here we are continuing because there is no change in value of attribute ",attr
                        continue
                    else:
                        if attr == 'inside' or attr == 'above' or attr == 'fill' or attr == 'size':
                            trans[i][attr] = attrB

                        elif attr == 'angle':
                            trans[i][attr] = int(attrB) - int(attrA)

                        elif attr == 'alignment':
                            avals = attrA.split('-')
                            bvals = attrB.split('-')
                            if avals[0] != bvals[0]:
                                trans[i][attr] = bvals[0]
                            elif avals[1] != bvals[1]:
                                trans[i][attr] = bvals[1]

                        else:
                            trans[i][attr] = attrB

                print trans

            #Logic to cover new objects that may have got added
            if bNoOfObjs > aNoOfObjs:
                b_rep = self.convertToForm(problem.figures['B'].objects)
                for bObjs in sorted(b_rep):
                    if trans.has_key(bObjs):
                        continue
                    else:
                        trans[bObjs] = {}
                        trans[bObjs]['type'] = 'add'
                        for attr in b_rep[bObjs].attributes:
                            trans[bObjs][attr] = b_rep[bObjs].attributes[attr]


            print "The final transformation representation for this Problem is:",trans

            c_rep = self.convertToForm(problem.figures['C'].objects)

            #Create the missing image representation using representation for C and the transformation matrix
            d_rep = {}
            for objs in c_rep:

                if trans.has_key(objs) and trans[objs] == 'delete':
                    print "This object in C gets deleted:",objs
                    print "Missing image at this stage is",d_rep
                    continue

                #A small checking for covering the outlier - Q12
                if 'delete' in trans.values() and c_rep[objs].attributes.has_key('inside'):
                    print "This object in C gets deleted:",objs
                    print "Missing image at this stage is",d_rep
                    continue

                d_rep[objs]={}

                for attr in c_rep[objs].attributes:
                    if trans.has_key(objs) and trans[objs].has_key(attr):
                        if trans[objs][attr] == 'delete':
                            print "Skip the attribute:",attr
                            continue

                        if attr == 'angle':
                            d_rep[objs][attr] = int(c_rep[objs].attributes[attr]) -  int(trans[objs][attr])
                            d_rep[objs][attr] = str(self.normalizeAngle(d_rep[objs][attr]))

                        elif attr == 'alignment':
                            d_rep[objs][attr] = self.getAlignment(c_rep[objs].attributes[attr], trans[objs][attr])

                        else:
                            d_rep[objs][attr] = trans[objs][attr]

                    else:
                        d_rep[objs][attr] = c_rep[objs].attributes[attr]

                print "Representation of missing image at this stage\n",d_rep

            #To factor in the added object
            for oneObj in trans:
                if not(isinstance(trans[oneObj],str)) and trans[oneObj].has_key('type'):
                    d_rep[oneObj] = {}
                    for attr in trans[oneObj]:
                        if attr == 'type':
                            continue
                        d_rep[oneObj][attr] = trans[oneObj][attr]

            print "Final representation of the missing image:\n",d_rep

            finalSolution = self.pickAnswer(problem, d_rep)
            print "The final solution to this Problem:",finalSolution
        except Exception as e:
            print "Skip this problem due to exception"
            print e
            finalSolution = -1

        return finalSolution

    def convertToForm(self, obj_dict):
        new_dict = {}
        i = 1

        for objs in sorted(obj_dict):
            new_dict[i] = obj_dict[objs]
            i+=1

        return new_dict

    def normalizeAngle(self, value):
        if value>360:
            return value%270
        return value

    def getAlignment(self, cAlignValue, transformation):
        finalAlignment = ""
        cArray = cAlignValue.split('-')
        if transformation == 'right' or transformation == 'left':
            finalAlignment = cArray[0]+'-'+transformation
        else:
            finalAlignment = transformation+'-'+cArray[1]

        return finalAlignment

    def pickAnswer(self, problem, d_rep):

        scores = []
        for i in xrange(1,7):
            figNum = str(i)
            oneChoice = self.convertToForm(problem.figures[figNum].objects)

            if len(d_rep) >= 3:
                print "Starting for choice",i
                currentScore = self.mapAndCompare(oneChoice, d_rep)
                print "score for option:",i

            else:
                print "Starting for choice",i
                currentScore = self.compareChoice(oneChoice, d_rep)
                print "score for option:",i

            print currentScore
            scores.append(currentScore)

        bestAnswer = scores.index(max(scores))+1
        return bestAnswer

    def compareChoice(self, oneChoice, d_rep):
        score = 0
        for objs in d_rep:

            if not (oneChoice.has_key(objs)):
                continue

            for attr in d_rep[objs]:
                if oneChoice[objs].attributes.has_key(attr) and d_rep[objs][attr] == oneChoice[objs].attributes[attr]:
                    score += 10

        return score

    def mapAndCompare(self, oneChoice, d_rep):
        score = 0
        for dObj in d_rep:
            for choiceObj in oneChoice:
                if not(d_rep[dObj].has_key('inside')) and not(oneChoice[choiceObj].attributes.has_key('inside')):
                    score += self.pairScore(d_rep[dObj], oneChoice[choiceObj].attributes)

                elif d_rep[dObj].has_key('inside') and oneChoice[choiceObj].attributes.has_key('inside') and len(d_rep[dObj]['inside']) == len(oneChoice[choiceObj].attributes['inside']):
                    score += self.pairScore(d_rep[dObj], oneChoice[choiceObj].attributes)

        return score

    def pairScore(self, dict1, dict2):
        score = 0
        for attr in dict1:
            if dict1[attr] == dict2[attr]:
                score += 10

        return score

    def getCorrObj(self, curObj, figure):

        for objs in figure.objects:
            print "getCorrObj() - Will now check corresponding using:",objs
            if self.matchObjs(curObj,figure.objects[objs]):
                return objs
        return

    def matchObjs(self, curObj, figureObj):

        if len(curObj.attributes) != len(figureObj.attributes):
            return False

        for attr in curObj.attributes:
            if not(figureObj.attributes.has_key(attr)):
                return False

            if attr == 'inside':
                if len(curObj.attributes[attr]) == len(figureObj.attributes[attr]):
                    print "Got a match for corresponding objects"
                    return True
                else:
                    return False

        print "Got a match for corresponding objects"
        return True

import os
import shutil


# A library to help keep data-driven project directories organized


class Workspace:
    def __init__(self, paths, verbosity=0):
        self.paths = paths
        self.verbosity = verbosity

        print('[workspace]: Instatiating workspace at "{}"'.format(os.getcwd())) if self.verbosity>=1 else False

        for path in self.paths:
            if not os.path.exists(path):
                print('[workspace]: Creating path "{}"'.format(path)) if self.verbosity>=2 else False
                os.mkdir(path)
            else:
                print('[workspace]: Path "{}" already exists'.format(path)) if self.verbosity>=2 else False


    def reset(self):
        '''
        Resets contents of workspace folders.
        '''

        print('[workspace]: Resetting workspace') if self.verbosity>=1 else False

        for path in self.paths:
            try:
                shutil.rmtree(path)
                print('[workspace]: Reset "{}"'.format(path)) if self.verbosity>=2 else False
            except:
                print('[workspace]: Unable to reset "{}"'.format(path)) if self.verbosity>=2 else False
            
            os.mkdir(path)



    def clear(self):
        '''
        Clears workspace folders.
        '''

        print('[workspace]: Clearing workspace') if self.verbosity>=1 else False
        
        for path in self.paths:
            try:
                shutil.rmtree(path)
                print('[workspace]: Removed "{}"'.format(path)) if self.verbosity>=2 else False
            except:
                print('[workspace]: Unable to remove "{}"'.format(path)) if self.verbosity>=2 else False


    def new(self, path):
        if not os.path.exists(path):
            print('[workspace]: Creating path "{}"'.format(path)) if self.verbosity>=1 else False
            os.mkdir(path)
            self.paths.append(path)
        else:
            print('[workspace]: Path "{}" already exists'.format(path)) if self.verbosity>=1 else False


    @staticmethod
    def getOpen(file_name, output_path, file_ext=''):
        '''
        Returns next available path name. Useful for batch data exports.
        '''

        base = output_path + '/' + file_name + '_'

        i = 0
        while os.path.exists(base + str(i) + file_ext):
            i += 1
        
        open_path = base + str(i) + file_ext


        return open_path


    @staticmethod
    def create(path):
        if not os.path.exists(path):
            print('[workspace]: Creating path "{}"'.format(path)) if self.verbosity>=1 else False
            os.mkdir(path)
            self.paths.append(path)
        else:
            print('[workspace]: Path "{}" already exists'.format(path)) if self.verbosity>=1 else False



if __name__ == '__main__':
    print('[workspace]: Running test...')
    ws = Workspace(paths=['folder_A','folder_A/subfolder','folder_B','folder_C'], verbosity=2)

    input('Press any key to clear workspace...')
    ws.clear()
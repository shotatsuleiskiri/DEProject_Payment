import myFramework.utils.utils as utils
from sqltostaging.initial.toStaging import ToStaging



if __name__ =="__main__":
    test = ToStaging("dvdrental", "public")
    tbname_Df = utils.getTbaleList(test.dbname,test.schema)['tablename']
    for tbname in tbname_Df:
        utils.fillstaging(utils.getDF(test.dbname, tbname, test.schema),"DBStaging","dvdrental",tbname)

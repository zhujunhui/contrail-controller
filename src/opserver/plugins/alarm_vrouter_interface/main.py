from  opserver.plugins.alarm_base import *

class VrouterInterface(AlarmBase):
    """Vrouter interface(s) in error state.
       VrouterAgent has interfaces in error state in VrouterAgent.error_intf_list"""

    def __call__(self, uve_key, uve_data):
        err_list = []
        if not uve_data.has_key("VrouterAgent"):
            return self.__class__.__name__, AlarmBase.SYS_WARN, err_list
        
        ust = uve_data["VrouterAgent"]

        if not ust.has_key("error_intf_list"):
            return self.__class__.__name__, AlarmBase.SYS_WARN, err_list

        if len(ust["error_intf_list"]):
            err_list.append(AlarmRule(oper="==",
                operand1=AlarmOperand(\
                    name="VrouterAgent.error_intf_list",
                    value=ust["error_intf_list"]),
                operand2=AlarmOperand(\
                    name=None,
                    value=None)))

        return self.__class__.__name__, AlarmBase.SYS_WARN, err_list 

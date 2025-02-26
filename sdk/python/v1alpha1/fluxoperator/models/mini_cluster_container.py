# coding: utf-8

"""
    fluxoperator

    Python SDK for Flux-Operator  # noqa: E501

    The version of the OpenAPI document: v1alpha1
    Generated by: https://openapi-generator.tech
"""


import inspect
import pprint
import re  # noqa: F401
import six

from fluxoperator.configuration import Configuration


class MiniClusterContainer(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'batch': 'bool',
        'command': 'str',
        'commands': 'Commands',
        'cores': 'int',
        'diagnostics': 'bool',
        'environment': 'dict(str, str)',
        'existing_volumes': 'dict(str, MiniClusterExistingVolume)',
        'flux_log_level': 'int',
        'flux_option_flags': 'str',
        'flux_user': 'FluxUser',
        'image': 'str',
        'image_pull_secret': 'str',
        'launcher': 'bool',
        'life_cycle': 'LifeCycle',
        'logs': 'str',
        'name': 'str',
        'ports': 'list[int]',
        'pre_command': 'str',
        'pull_always': 'bool',
        'resources': 'ContainerResources',
        'run_flux': 'bool',
        'security_context': 'SecurityContext',
        'volumes': 'dict(str, ContainerVolume)',
        'working_dir': 'str'
    }

    attribute_map = {
        'batch': 'batch',
        'command': 'command',
        'commands': 'commands',
        'cores': 'cores',
        'diagnostics': 'diagnostics',
        'environment': 'environment',
        'existing_volumes': 'existingVolumes',
        'flux_log_level': 'fluxLogLevel',
        'flux_option_flags': 'fluxOptionFlags',
        'flux_user': 'fluxUser',
        'image': 'image',
        'image_pull_secret': 'imagePullSecret',
        'launcher': 'launcher',
        'life_cycle': 'lifeCycle',
        'logs': 'logs',
        'name': 'name',
        'ports': 'ports',
        'pre_command': 'preCommand',
        'pull_always': 'pullAlways',
        'resources': 'resources',
        'run_flux': 'runFlux',
        'security_context': 'securityContext',
        'volumes': 'volumes',
        'working_dir': 'workingDir'
    }

    def __init__(self, batch=False, command='', commands=None, cores=0, diagnostics=False, environment=None, existing_volumes=None, flux_log_level=6, flux_option_flags='', flux_user=None, image='ghcr.io/rse-ops/accounting:app-latest', image_pull_secret='', launcher=False, life_cycle=None, logs='', name='', ports=None, pre_command='', pull_always=False, resources=None, run_flux=False, security_context=None, volumes=None, working_dir='', local_vars_configuration=None):  # noqa: E501
        """MiniClusterContainer - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._batch = None
        self._command = None
        self._commands = None
        self._cores = None
        self._diagnostics = None
        self._environment = None
        self._existing_volumes = None
        self._flux_log_level = None
        self._flux_option_flags = None
        self._flux_user = None
        self._image = None
        self._image_pull_secret = None
        self._launcher = None
        self._life_cycle = None
        self._logs = None
        self._name = None
        self._ports = None
        self._pre_command = None
        self._pull_always = None
        self._resources = None
        self._run_flux = None
        self._security_context = None
        self._volumes = None
        self._working_dir = None
        self.discriminator = None

        if batch is not None:
            self.batch = batch
        if command is not None:
            self.command = command
        if commands is not None:
            self.commands = commands
        if cores is not None:
            self.cores = cores
        if diagnostics is not None:
            self.diagnostics = diagnostics
        if environment is not None:
            self.environment = environment
        if existing_volumes is not None:
            self.existing_volumes = existing_volumes
        if flux_log_level is not None:
            self.flux_log_level = flux_log_level
        if flux_option_flags is not None:
            self.flux_option_flags = flux_option_flags
        if flux_user is not None:
            self.flux_user = flux_user
        if image is not None:
            self.image = image
        if image_pull_secret is not None:
            self.image_pull_secret = image_pull_secret
        if launcher is not None:
            self.launcher = launcher
        if life_cycle is not None:
            self.life_cycle = life_cycle
        if logs is not None:
            self.logs = logs
        if name is not None:
            self.name = name
        if ports is not None:
            self.ports = ports
        if pre_command is not None:
            self.pre_command = pre_command
        if pull_always is not None:
            self.pull_always = pull_always
        if resources is not None:
            self.resources = resources
        if run_flux is not None:
            self.run_flux = run_flux
        if security_context is not None:
            self.security_context = security_context
        if volumes is not None:
            self.volumes = volumes
        if working_dir is not None:
            self.working_dir = working_dir

    @property
    def batch(self):
        """Gets the batch of this MiniClusterContainer.  # noqa: E501

        Indicate that the command is a batch job that will be written to a file to submit  # noqa: E501

        :return: The batch of this MiniClusterContainer.  # noqa: E501
        :rtype: bool
        """
        return self._batch

    @batch.setter
    def batch(self, batch):
        """Sets the batch of this MiniClusterContainer.

        Indicate that the command is a batch job that will be written to a file to submit  # noqa: E501

        :param batch: The batch of this MiniClusterContainer.  # noqa: E501
        :type batch: bool
        """

        self._batch = batch

    @property
    def command(self):
        """Gets the command of this MiniClusterContainer.  # noqa: E501

        Single user executable to provide to flux start  # noqa: E501

        :return: The command of this MiniClusterContainer.  # noqa: E501
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this MiniClusterContainer.

        Single user executable to provide to flux start  # noqa: E501

        :param command: The command of this MiniClusterContainer.  # noqa: E501
        :type command: str
        """

        self._command = command

    @property
    def commands(self):
        """Gets the commands of this MiniClusterContainer.  # noqa: E501


        :return: The commands of this MiniClusterContainer.  # noqa: E501
        :rtype: Commands
        """
        return self._commands

    @commands.setter
    def commands(self, commands):
        """Sets the commands of this MiniClusterContainer.


        :param commands: The commands of this MiniClusterContainer.  # noqa: E501
        :type commands: Commands
        """

        self._commands = commands

    @property
    def cores(self):
        """Gets the cores of this MiniClusterContainer.  # noqa: E501

        Cores the container should use  # noqa: E501

        :return: The cores of this MiniClusterContainer.  # noqa: E501
        :rtype: int
        """
        return self._cores

    @cores.setter
    def cores(self, cores):
        """Sets the cores of this MiniClusterContainer.

        Cores the container should use  # noqa: E501

        :param cores: The cores of this MiniClusterContainer.  # noqa: E501
        :type cores: int
        """

        self._cores = cores

    @property
    def diagnostics(self):
        """Gets the diagnostics of this MiniClusterContainer.  # noqa: E501

        Run flux diagnostics on start instead of command  # noqa: E501

        :return: The diagnostics of this MiniClusterContainer.  # noqa: E501
        :rtype: bool
        """
        return self._diagnostics

    @diagnostics.setter
    def diagnostics(self, diagnostics):
        """Sets the diagnostics of this MiniClusterContainer.

        Run flux diagnostics on start instead of command  # noqa: E501

        :param diagnostics: The diagnostics of this MiniClusterContainer.  # noqa: E501
        :type diagnostics: bool
        """

        self._diagnostics = diagnostics

    @property
    def environment(self):
        """Gets the environment of this MiniClusterContainer.  # noqa: E501

        Key/value pairs for the environment  # noqa: E501

        :return: The environment of this MiniClusterContainer.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this MiniClusterContainer.

        Key/value pairs for the environment  # noqa: E501

        :param environment: The environment of this MiniClusterContainer.  # noqa: E501
        :type environment: dict(str, str)
        """

        self._environment = environment

    @property
    def existing_volumes(self):
        """Gets the existing_volumes of this MiniClusterContainer.  # noqa: E501

        Existing Volumes to add to the containers  # noqa: E501

        :return: The existing_volumes of this MiniClusterContainer.  # noqa: E501
        :rtype: dict(str, MiniClusterExistingVolume)
        """
        return self._existing_volumes

    @existing_volumes.setter
    def existing_volumes(self, existing_volumes):
        """Sets the existing_volumes of this MiniClusterContainer.

        Existing Volumes to add to the containers  # noqa: E501

        :param existing_volumes: The existing_volumes of this MiniClusterContainer.  # noqa: E501
        :type existing_volumes: dict(str, MiniClusterExistingVolume)
        """

        self._existing_volumes = existing_volumes

    @property
    def flux_log_level(self):
        """Gets the flux_log_level of this MiniClusterContainer.  # noqa: E501

        Log level to use for flux logging (only in non TestMode)  # noqa: E501

        :return: The flux_log_level of this MiniClusterContainer.  # noqa: E501
        :rtype: int
        """
        return self._flux_log_level

    @flux_log_level.setter
    def flux_log_level(self, flux_log_level):
        """Sets the flux_log_level of this MiniClusterContainer.

        Log level to use for flux logging (only in non TestMode)  # noqa: E501

        :param flux_log_level: The flux_log_level of this MiniClusterContainer.  # noqa: E501
        :type flux_log_level: int
        """

        self._flux_log_level = flux_log_level

    @property
    def flux_option_flags(self):
        """Gets the flux_option_flags of this MiniClusterContainer.  # noqa: E501

        Flux option flags, usually provided with -o optional - if needed, default option flags for the server These can also be set in the user interface to override here. This is only valid for a FluxRunner \"runFlux\" true  # noqa: E501

        :return: The flux_option_flags of this MiniClusterContainer.  # noqa: E501
        :rtype: str
        """
        return self._flux_option_flags

    @flux_option_flags.setter
    def flux_option_flags(self, flux_option_flags):
        """Sets the flux_option_flags of this MiniClusterContainer.

        Flux option flags, usually provided with -o optional - if needed, default option flags for the server These can also be set in the user interface to override here. This is only valid for a FluxRunner \"runFlux\" true  # noqa: E501

        :param flux_option_flags: The flux_option_flags of this MiniClusterContainer.  # noqa: E501
        :type flux_option_flags: str
        """

        self._flux_option_flags = flux_option_flags

    @property
    def flux_user(self):
        """Gets the flux_user of this MiniClusterContainer.  # noqa: E501


        :return: The flux_user of this MiniClusterContainer.  # noqa: E501
        :rtype: FluxUser
        """
        return self._flux_user

    @flux_user.setter
    def flux_user(self, flux_user):
        """Sets the flux_user of this MiniClusterContainer.


        :param flux_user: The flux_user of this MiniClusterContainer.  # noqa: E501
        :type flux_user: FluxUser
        """

        self._flux_user = flux_user

    @property
    def image(self):
        """Gets the image of this MiniClusterContainer.  # noqa: E501

        Container image must contain flux and flux-sched install  # noqa: E501

        :return: The image of this MiniClusterContainer.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this MiniClusterContainer.

        Container image must contain flux and flux-sched install  # noqa: E501

        :param image: The image of this MiniClusterContainer.  # noqa: E501
        :type image: str
        """

        self._image = image

    @property
    def image_pull_secret(self):
        """Gets the image_pull_secret of this MiniClusterContainer.  # noqa: E501

        Allow the user to pull authenticated images By default no secret is selected. Setting this with the name of an already existing imagePullSecret will specify that secret in the pod spec.  # noqa: E501

        :return: The image_pull_secret of this MiniClusterContainer.  # noqa: E501
        :rtype: str
        """
        return self._image_pull_secret

    @image_pull_secret.setter
    def image_pull_secret(self, image_pull_secret):
        """Sets the image_pull_secret of this MiniClusterContainer.

        Allow the user to pull authenticated images By default no secret is selected. Setting this with the name of an already existing imagePullSecret will specify that secret in the pod spec.  # noqa: E501

        :param image_pull_secret: The image_pull_secret of this MiniClusterContainer.  # noqa: E501
        :type image_pull_secret: str
        """

        self._image_pull_secret = image_pull_secret

    @property
    def launcher(self):
        """Gets the launcher of this MiniClusterContainer.  # noqa: E501

        Indicate that the command is a launcher that will ask for its own jobs (and provided directly to flux start)  # noqa: E501

        :return: The launcher of this MiniClusterContainer.  # noqa: E501
        :rtype: bool
        """
        return self._launcher

    @launcher.setter
    def launcher(self, launcher):
        """Sets the launcher of this MiniClusterContainer.

        Indicate that the command is a launcher that will ask for its own jobs (and provided directly to flux start)  # noqa: E501

        :param launcher: The launcher of this MiniClusterContainer.  # noqa: E501
        :type launcher: bool
        """

        self._launcher = launcher

    @property
    def life_cycle(self):
        """Gets the life_cycle of this MiniClusterContainer.  # noqa: E501


        :return: The life_cycle of this MiniClusterContainer.  # noqa: E501
        :rtype: LifeCycle
        """
        return self._life_cycle

    @life_cycle.setter
    def life_cycle(self, life_cycle):
        """Sets the life_cycle of this MiniClusterContainer.


        :param life_cycle: The life_cycle of this MiniClusterContainer.  # noqa: E501
        :type life_cycle: LifeCycle
        """

        self._life_cycle = life_cycle

    @property
    def logs(self):
        """Gets the logs of this MiniClusterContainer.  # noqa: E501

        Log output directory  # noqa: E501

        :return: The logs of this MiniClusterContainer.  # noqa: E501
        :rtype: str
        """
        return self._logs

    @logs.setter
    def logs(self, logs):
        """Sets the logs of this MiniClusterContainer.

        Log output directory  # noqa: E501

        :param logs: The logs of this MiniClusterContainer.  # noqa: E501
        :type logs: str
        """

        self._logs = logs

    @property
    def name(self):
        """Gets the name of this MiniClusterContainer.  # noqa: E501

        Container name is only required for non flux runners  # noqa: E501

        :return: The name of this MiniClusterContainer.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MiniClusterContainer.

        Container name is only required for non flux runners  # noqa: E501

        :param name: The name of this MiniClusterContainer.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def ports(self):
        """Gets the ports of this MiniClusterContainer.  # noqa: E501

        Ports to be exposed to other containers in the cluster We take a single list of integers and map to the same  # noqa: E501

        :return: The ports of this MiniClusterContainer.  # noqa: E501
        :rtype: list[int]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this MiniClusterContainer.

        Ports to be exposed to other containers in the cluster We take a single list of integers and map to the same  # noqa: E501

        :param ports: The ports of this MiniClusterContainer.  # noqa: E501
        :type ports: list[int]
        """

        self._ports = ports

    @property
    def pre_command(self):
        """Gets the pre_command of this MiniClusterContainer.  # noqa: E501

        Special command to run at beginning of script, directly after asFlux is defined as sudo -u flux -E (so you can change that if desired.) This is only valid if FluxRunner is set (that writes a wait.sh script) This is for the indexed job pods and the certificate generation container.  # noqa: E501

        :return: The pre_command of this MiniClusterContainer.  # noqa: E501
        :rtype: str
        """
        return self._pre_command

    @pre_command.setter
    def pre_command(self, pre_command):
        """Sets the pre_command of this MiniClusterContainer.

        Special command to run at beginning of script, directly after asFlux is defined as sudo -u flux -E (so you can change that if desired.) This is only valid if FluxRunner is set (that writes a wait.sh script) This is for the indexed job pods and the certificate generation container.  # noqa: E501

        :param pre_command: The pre_command of this MiniClusterContainer.  # noqa: E501
        :type pre_command: str
        """

        self._pre_command = pre_command

    @property
    def pull_always(self):
        """Gets the pull_always of this MiniClusterContainer.  # noqa: E501

        Allow the user to dictate pulling By default we pull if not present. Setting this to true will indicate to pull always  # noqa: E501

        :return: The pull_always of this MiniClusterContainer.  # noqa: E501
        :rtype: bool
        """
        return self._pull_always

    @pull_always.setter
    def pull_always(self, pull_always):
        """Sets the pull_always of this MiniClusterContainer.

        Allow the user to dictate pulling By default we pull if not present. Setting this to true will indicate to pull always  # noqa: E501

        :param pull_always: The pull_always of this MiniClusterContainer.  # noqa: E501
        :type pull_always: bool
        """

        self._pull_always = pull_always

    @property
    def resources(self):
        """Gets the resources of this MiniClusterContainer.  # noqa: E501


        :return: The resources of this MiniClusterContainer.  # noqa: E501
        :rtype: ContainerResources
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this MiniClusterContainer.


        :param resources: The resources of this MiniClusterContainer.  # noqa: E501
        :type resources: ContainerResources
        """

        self._resources = resources

    @property
    def run_flux(self):
        """Gets the run_flux of this MiniClusterContainer.  # noqa: E501

        Main container to run flux (only should be one)  # noqa: E501

        :return: The run_flux of this MiniClusterContainer.  # noqa: E501
        :rtype: bool
        """
        return self._run_flux

    @run_flux.setter
    def run_flux(self, run_flux):
        """Sets the run_flux of this MiniClusterContainer.

        Main container to run flux (only should be one)  # noqa: E501

        :param run_flux: The run_flux of this MiniClusterContainer.  # noqa: E501
        :type run_flux: bool
        """

        self._run_flux = run_flux

    @property
    def security_context(self):
        """Gets the security_context of this MiniClusterContainer.  # noqa: E501


        :return: The security_context of this MiniClusterContainer.  # noqa: E501
        :rtype: SecurityContext
        """
        return self._security_context

    @security_context.setter
    def security_context(self, security_context):
        """Sets the security_context of this MiniClusterContainer.


        :param security_context: The security_context of this MiniClusterContainer.  # noqa: E501
        :type security_context: SecurityContext
        """

        self._security_context = security_context

    @property
    def volumes(self):
        """Gets the volumes of this MiniClusterContainer.  # noqa: E501

        Volumes that can be mounted (must be defined in volumes)  # noqa: E501

        :return: The volumes of this MiniClusterContainer.  # noqa: E501
        :rtype: dict(str, ContainerVolume)
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """Sets the volumes of this MiniClusterContainer.

        Volumes that can be mounted (must be defined in volumes)  # noqa: E501

        :param volumes: The volumes of this MiniClusterContainer.  # noqa: E501
        :type volumes: dict(str, ContainerVolume)
        """

        self._volumes = volumes

    @property
    def working_dir(self):
        """Gets the working_dir of this MiniClusterContainer.  # noqa: E501

        Working directory to run command from  # noqa: E501

        :return: The working_dir of this MiniClusterContainer.  # noqa: E501
        :rtype: str
        """
        return self._working_dir

    @working_dir.setter
    def working_dir(self, working_dir):
        """Sets the working_dir of this MiniClusterContainer.

        Working directory to run command from  # noqa: E501

        :param working_dir: The working_dir of this MiniClusterContainer.  # noqa: E501
        :type working_dir: str
        """

        self._working_dir = working_dir

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = inspect.getargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MiniClusterContainer):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MiniClusterContainer):
            return True

        return self.to_dict() != other.to_dict()
